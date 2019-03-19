x, y = 1 + 2, 100                  # (3, 100)
                                   # 
1 + 3 # foo                        # 4

x; y
                                   # 
def fib(n):                        # 
  if n < 2:                        # 
    return n                       # 0
  else:                            # 
    return fib(n - 1) + fib(n - 2) # 3
                                   # 
def foo():                         # 
  return "hello" + "foo"           # 'hellofoo'
                                   # 
print('foo result', foo())         # 
                                   # 
foo()                              # 'hellofoo'
fib(10)                            # 55
fib(4)                             # 3
1 + 2                              # 3
# foo result hellofoo
