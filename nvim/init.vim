call plug#begin('~/.nvim/plugged')
    " Comment code
    Plug 'tpope/vim-commentary'

    if exists('g:vscode')
        " Easy motion for VSCode
        Plug 'asvetliakov/vim-easymotion'
        "Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
        "Plug 'Shougo/neco-syntax'
    else
        Plug 'sirver/ultisnips'
        Plug 'honza/vim-snippets'
        
        " Syntax support
        Plug 'sheerun/vim-polyglot'
        " Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
        " Autopairs
        Plug 'jiangmiao/auto-pairs'
        " File explorer
        Plug 'scrooloose/NERDTree'    
        " Icons
        Plug 'ryanoasis/vim-devicons'
        " Intellisense
        Plug 'neoclide/coc.nvim', {'branch': 'release'}
        " Airline
        Plug 'vim-airline/vim-airline'
        Plug 'vim-airline/vim-airline-themes'
        
        Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
        Plug 'Shougo/neco-syntax'
        
        " Indent guides
        " Plug 'Yggdroot/indentLine' 
        " Git integration
        Plug 'mhinz/vim-signify'
        " Autoclose tags
        Plug 'alvan/vim-closetag'
        " Ranger
        Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
        " Fzf
        Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
        Plug 'junegunn/fzf.vim'
        Plug 'airblade/vim-rooter'
        " Prettier
        Plug 'prettier/vim-prettier', { 'do': 'yarn install' }

        " Themes
        Plug 'joshdick/onedark.vim'
        Plug 'kaicataldo/material.vim'
        Plug 'tomasiser/vim-code-dark'
        Plug 'crusoexia/vim-monokai'
        Plug 'ayu-theme/ayu-vim'
        Plug 'dracula/vim', { 'as': 'dracula' }
    endif
call plug#end()

let g:airline#extensions#tabline#enabled = 1  " Mostrar buffers abiertos (como pestañas)
let g:airline#extensions#tabline#fnamemod = ':t'  " Mostrar sólo el nombre del archivo

" Cargar fuente Powerline y símbolos (ver nota)
let g:airline_powerline_fonts = 1

"set noshowmode

"let g:deoplete#enable_at_startup = 1

"augroup deopleteCompleteDoneAu
  "autocmd!
  "autocmd CompleteDone * silent! pclose!
"augroup END


let g:UltiSnipsExpandTrigger = '<c-j>'

" Ir a siguiente ubicacion con Ctrl + j
let g:UltiSnipsJumpForwardTrigger = '<c-j>'
" Ir a anterior ubicacion con Ctrl + k
let g:UltiSnipsJumpBackwardTrigger = '<c-k>'
