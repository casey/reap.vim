```
*reap.vim* / *rave.imp* (R)ead (E)val (A)nnotate (P)rint [Python!]

                       ____  _________    ____        _
                      / __ \/ ____/   |  / __ \_   __(_)___ ___
                     / /_/ / __/ / /| | / /_/ / | / / / __ `__ \
                    / _, _/ /___/ ___ |/ ____/| |/ / / / / / / /
                   /_/ |_/_____/_/  |_/_/   (_)___/_/_/ /_/ /_/

                        (R)ead (E)val (A)nnotate (P)rint

                                By Casey Rodarmor
                            mailto:casey@rodarmor.com

CONTENTS                                                   
==============================================================================

0. Magnasanti
1. Intro
2. Usage
3. Configuration
4. License
5. Contributing
6. Wishlist
7. Changelog
8. Grid


MAGNASANTI                                    
------------------------------------------------------------------------------

                         ALL ROADS LEAD TO MAGNASANTI

                                  ██████████
                              ████          ████
                            ██        ██        ██
                          ██      ██  ██  ██      ██
                        ██    ██  ████  ████  ██    ██
                        ██      ██  ██  ██  ██      ██
                      ██    ████    ██████    ████    ██
                      ██      ██████  ██  ██████      ██
                      ██  ████    ████  ████    ████  ██
                      ██      ██████  ██  ██████      ██
                      ██    ████    ██████    ████    ██
                        ██      ██  ██  ██  ██      ██
                        ██    ██  ████  ████  ██    ██
                          ██      ██  ██  ██      ██
                            ██        ██        ██
                              ████          ████
                                  ██████████

                         https://youtu.be/NTJQTc-TqpU


INTRO                                                        
------------------------------------------------------------------------------

Reap.vim hijacks the = operator to run Python 3 source code directly from vim
buffers, annotating it with values and ouput.

A demonstration is online here: https://youtu.be/BNYddRCqfSY

Use ={motion} on the code you want to run, or == to evaluate the current line.

Reap is provided as a plugin, available at `github.com/casey/reap.vim`. A nice
tool to manage your Vim plugins is vim-plug:

https://github.com/junegunn/vim-plug

If you use vim-plug, add the following to your .vimrc and run `:PlugUpdate`:
>
 Plug 'casey/reap.vim'

Reap expects a `python3` binary to be in the `$PATH`.


USAGE                                                        
------------------------------------------------------------------------------

Reap annotates expressions and assignments in Python 3 code with their values:
>
  1 + 1             # 2
                    #
  tau = 2 * math.pi # 6.283185307179586
                    #
  x = 'foo' + 'bar' # 'foobar'

If an expression is evaluated more than once, it will be annotated with the
most recent value:
>
  def fib(n):                        #
    if n < 2:                        #
      return n                       # 0
    else:                            #
      return fib(n - 1) + fib(n - 2) # 55
                                     #
  fib(10)                            # 55

Reap works by setting 'equalprg' to the included ``reap.py`` script, which
runs and annotates Python 3 source code. 'equalprg' determines the program
used to filter text passed to the = operator, and is conventionally set to a
formatting utility.


CONFIGURATION                                        
------------------------------------------------------------------------------

Reap is not configurable, although it should be. See |ReapWishlist|.


------------------------------------------------------------------------------
LICENSE                                                    

Informally, do what thou wilt shall be the whole of the license.

Formally, `reap.vim` is dedicated to the public domain with the CC0 public
domain dedication.


CONTRIBUTING                                          
------------------------------------------------------------------------------

Reap is developed on GitHub at https://github.com/casey/reap.vim. Please feel
free to open issues with feature requests and bug reports.


WISHLIST                                                  
------------------------------------------------------------------------------

There are lots of things that Reap should do:

- Configure the operator, allowing un-hijacking = and 'equalprg'

- Use the integrated Python 3 interpreter, if Vim is compiled with one.

- Support languages other than Python

- Be available as a command, i.e. `:Reap`, as well as an operator.

- Annotate if, for, yield, raise, assert, and while statements

- Expose the options that `reap.py` takes as configuration

Pull-requests with implementations of the above are most welcome!


CHANGELOG                                                
------------------------------------------------------------------------------

## [0.0.0] - 2019-03-21
### Added
- Initial public version


GRID                                           
------------------------------------------------------------------------------

            ╾╼░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░╾╼                        ╾╼
              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░
              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░
              ░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░
              ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
              ████▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
              ████▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░
              ░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░
            ╾╼░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░╾╼░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░╾╼
            ░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░
            ░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░
            ░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░
            ░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
            ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░
            ░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░
            ░░░░░░░░▒▒▒▒████▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░
            ╾╼                        ╾╼░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░╾╼

                           Tʜᴇ sᴜᴘᴇʀɪᴏʀ 12x12 ɢʀɪᴅ
                        ᴇᴍᴘʟᴏʏᴇᴅ ɪɴ Mᴀɢɴᴀsᴀɴᴛɪ ᴄᴀɴɴᴏᴛ
                                ʙᴇ ʙᴇᴀᴛᴇɴ >:]


==============================================================================
```
