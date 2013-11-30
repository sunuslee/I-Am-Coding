" auto save plugin for I Am Coding

autocmd BufCreate,BufEnter * silent call IAC_init()
autocmd CursorHold,CursorHoldI,CursorMoved,CursorMovedI * silent call IAC_updatefile()


function! IAC_init()
    let s:IAC_lastupdate = localtime()
    let s:IAC_updateInterval = 4
endfunction

" send file contents to local server
" data format is like this:
" filename
" line1-of-file
" line2-of-file
" ...
function! IAC_updatefile()
    let IAC_now=localtime()
    if IAC_now - s:IAC_lastupdate > s:IAC_updateInterval
        execute 'silent! write'
        let filaname=expand('%:p')
        let current_buffer = [filaname] + getbufline("%", 1, "$")
        let data = join(current_buffer, "\n")
        let data = escape(shellescape(data), "%!#")
        let cmd='silent! !curl -POST -s -d ' . data . ' localhost:7375 2>&1 > /dev/null &'
        silent! execute cmd
        let s:IAC_lastupdate = IAC_now
    endif
endfunction
