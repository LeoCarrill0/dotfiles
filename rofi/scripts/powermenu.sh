#!/bin/bash

rofi_command="rofi -theme themes/icons.rasi -p "power""

#### Options ###
power_off=""
reboot="ﰇ"
lock=""
suspend=""
log_out="﫼"
# Variable passed to rofi
options="$power_off\n$reboot\n$lock\n$suspend\n$log_out"

chosen="$(echo -e "$options" | $rofi_command -dmenu -selected-row 6)"
case $chosen in
    $lock)
        setxkbmap us -option caps:escape && betterlockscreen -l dimblur -t "leocarrillo"
        ;;    
    $power_off)
        systemctl poweroff
        ;;
    $reboot)
        systemctl reboot
        ;;
    $suspend)
	    systemctl suspend
        ;;
    $log_out)
        bspc quit
        ;;
esac

