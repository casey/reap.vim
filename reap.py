#!/usr/bin/env python3

import ast, io, contextlib, argparse

import sys, math, string, time, random, re, itertools, os, logging, traceback, collections

marker = '#\xA0'

line_re = re.compile(
  r'''
    ^
    (?P<code>.*?)
    (?P<space>[ \t]*)
    (?P<annotation>([#]\xA0.*)?)
    (?P<end>\n|\r\n|)
    $
  ''',
  re.VERBOSE,
)

values = {}

def positive(value):
  i = int(value)
  if i < 1:
    raise argparse.ArgumentTypeError('value must be positive')
  return i

parser = argparse.ArgumentParser()
parser.add_argument(
  '--no-annotations',
  help='turn off value annotations',
  action='store_true',
)
parser.add_argument(
  '--no-output',
  help='do not append output written to stdout',
  action='store_true',
)
parser.add_argument(
  '--history',
  help='number of values to include in annotations',
  type=positive,
  default=1,
)
parser.add_argument(
  '--verbose',
  help='bloviate',
  action='store_true',
)
args = parser.parse_args()

output_sink = io.StringIO()

if args.no_output:
  stdout_sink = io.StringIO()
else:
  stdout_sink = output_sink

def tap(value, line, offset):
  if value != None:
    offsets = values.setdefault(line, {})
    history = offsets.setdefault(offset, [])
    history.append(value)
  return value

class Tap(ast.NodeTransformer):
  def rewrite(self, value, lineno, col_offset):
    return ast.Call(
      func=ast.Name('tap', ctx=ast.Load()),
      args=[self.generic_visit(value), ast.Num(n=lineno - 1), ast.Num(n=col_offset)],
      keywords=[],
    )

  def visit_Assign(self, original):
    replacement = self.rewrite(original.value, original.lineno, original.col_offset)
    return ast.Assign(targets=original.targets, value=replacement)

  def visit_Expr(self, original):
    replacement = self.rewrite(original.value, original.lineno, original.col_offset)
    return ast.Expr(value=replacement)

  def visit_Return(self, original):
    replacement = self.rewrite(original.value, original.lineno, original.col_offset)
    return ast.Return(value=replacement)

text = sys.stdin.read()

with contextlib.redirect_stdout(stdout_sink):
  with contextlib.redirect_stderr(output_sink):
    try:
      module = ast.parse(text, filename='<input>', mode='exec')
      rewrite = Tap().visit(module)
      fixed = ast.fix_missing_locations(rewrite)
      code = compile(rewrite, filename='<input>', mode='exec')
      exec(code)
    except:
      print(traceback.format_exc())

class Line:
  def __init__(self, index, code, space, annotation, end, values):
    self.index      = index
    self.code       = code
    self.space      = space
    self.annotation = annotation
    self.end        = end
    self.values     = values

  def __repr__(self):
    return f'{self.index}: {repr(self.code)} {repr(self.space)} {repr(self.annotation)} {repr(self.end)}, {repr(self.values)}'

  def width(self):
    return len(self.code)

  def format(self, width):
    if args.no_annotations:
      return f'{self.code}{self.end}'
    else:
      annotation = '; '.join([
        ', '.join([repr(value) for value in history[-args.history:]])
        for offset, history in sorted(self.values.items())
      ])
      return f'{self.code: <{width}} {marker}{annotation}{self.end}'

lines = list(
  Line(index=i, values=values.get(i, {}), **line_re.match(line).groupdict())
  for i, line
  in enumerate(text.splitlines(True))
)

if args.verbose:
  for line in lines:
    sys.stderr.write(f'{line.index}: ')
    sys.stderr.write(f'{repr(line.code)}, ')
    sys.stderr.write(f'{repr(line.space)}, ')
    sys.stderr.write(f'{repr(line.annotation)}, ')
    sys.stderr.write(f'{repr(line.end)}, ')
    sys.stderr.write(os.linesep)

output = output_sink.getvalue()

width = max((line.width() for line in lines), default=0)

for line in lines:
  sys.stdout.write(line.format(width))

if output and lines and not lines[-1].end:
  sys.stdout.write(os.linesep)

for line in output.splitlines(True):
  if line.rstrip():
    sys.stdout.write(marker)
    sys.stdout.write(line)
