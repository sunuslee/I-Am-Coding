" auto save plugin for I Am Coding

autocmd BufCreate,BufEnter * silent call IAC_init()
autocmd CursorHold,CursorHoldI,CursorMoved,CursorMovedI * silent call IAC_updatefile()

function! IAC_init()
    let s:IAC_lastupdate = localtime()
    let s:IAC_updateInterval = 4
endfunction

function! IAC_updatefile()
    let IAC_now=localtime()
    if IAC_now - s:IAC_lastupdate > s:IAC_updateInterval
        execute 'write'
    endif
endfunction
