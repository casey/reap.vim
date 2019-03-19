" set equalprg execute reap,py
let &equalprg = "python3 ".shellescape(expand('<sfile>:p:h:h')."/reap.py")
