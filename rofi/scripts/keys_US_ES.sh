#!usr/bin/env bash

set a (setxkbmap us -print | grep xkb_symbols)
echo "$a"
