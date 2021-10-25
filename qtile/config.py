# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal #, get_alternatives

#from lib.utils import get_alternatives, execute

from libqtile.log_utils import logger
from settings.path import qtile_path
from settings.theme import colors

from libqtile import hook

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

def Wifi_rofi():
    subprocess.call([path.join(qtile_path, '/home/leocarrillo/.config/rofi/scripts/rofi-wifi-menu.sh')])
def Power_rofi():
    subprocess.call([path.join(qtile_path, '/home/leocarrillo/.config/rofi/scripts/powermenu.sh')])
def Apps_rofi():
    subprocess.call([path.join(qtile_path, '/home/leocarrillo/.config/rofi/scripts/appsmenu.sh')])


mod = "mod4"
#terminal = get_alternatives(['terminator', 'gnome-terminal', 'xterm'])
terminal = "alacritty"
color = "#302569"
color_light = "#4A4469"
color_light2 = "#4A4469"
back = "#222222"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "control"], "l", lazy.layout.grow()),
    ([mod, "control"], "h", lazy.layout.shrink()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.screen.next_group()),
    ([mod], "comma", lazy.screen.prev_group()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("sh /home/leocarrillo/.config/rofi/scripts/appsmenu.sh")),
    #([mod], "m", lazy.spawn("rofi -show drun"))

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("google-chrome")),

    # File Explorer
    ([mod], "e", lazy.spawn("nautilus")),

    # Terminal
    ([mod], "Return", lazy.spawn(terminal)),

    #Key US | ES
    ([mod], "space", lazy.spawn("setxkbmap es -option caps:escape")),
    ([mod, "control"], "space", lazy.spawn("setxkbmap us -option caps:escape")),

    # Redshift e5ff
    ([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_font="Cantarell-14",
        dmenu_prompt="Ejecuta",
        background=back,
        foreground="#495469",
        selected_background="#637d8b",
        selected_foregorund="#FFFFFF",
        ))),

    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([], "Print", lazy.spawn("scrot 'Debian-%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir PICTURES)'")),
    ([mod], "Print", lazy.spawn('xfce4-screenshooter')),
    ([mod, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

    # ------------ Hardware Configs ------------

    #([mod], "p", lazy.spawn("alacritty")),

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]

# keys = [
#     ([mod], "r", lazy.run_extension(extension.DmenuRun(
#         dmenu_prompt="Ejecuta",
#         dmenu_font="Cantarell-16",
#         background=back,
#         foreground=color_light,
#         selected_background=color,
#         selected_foregorund="#ddd",
#         ))),
# ]

__groups = {
    1: Group("   ", matches=[Match(wm_class=["firefox", "google-chrome"])]),
    2: Group("   ", matches=[Match(wm_class=["jetbrains-pycharm-ce"])]),
    3: Group("   ", matches=[Match(wm_class=["konsole","Alacritty"])]),
    4: Group("   ", matches=[Match(wm_class=["code-oss", "arduino ide"])]),
    5: Group("   ", matches=[Match(wm_class=["blueman-manager", "gnome-control-center"])]),
    6: Group("   ", matches=[Match(wm_class=["org.gnome.Nautilus","thunar","Nemo"])]),
    7: Group("   ", matches=[Match(wm_class=["eog"])]),
    8: Group("   ", matches=[Match(wm_class=["kaffeine", "mpv", "org-tlauncher-tlauncher-rmo-TLauncher"])]),
    9: Group("   ", matches=[Match(wm_class=["okular","libreoffice","libreoffice-writer", "simple-scan"])]),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], str(get_group_key(i.name)),
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus=colors["color4"][0]
)

# layouts = [
#     #layout.Columns(border_focus_stack='#d75f5f'),
#     #layout.Max(),
#     # Try more layouts by unleashing below layouts.
#     #layout.Stack(num_stacks=2),
#     #layout.Bsp(),
#     #layout.Matrix(),
#     layout.MonadTall(
#         border_normal="#302569",#"#222222",
#         border_focus="#4A4469",#"#ff4400",
#         border_width=3,
#         single_border_width=0,
#         margin=6,
#         single_margin=0,
#     ),
#     #layout.MonadTall(),
#     #layout.MonadWide(),
#     #layout.RatioTile(),
#     #layout.Tile(),
#     #layout.TreeTab(),
#     #layout.VerticalTile(),
#     #layout.Zoomy(),
# ]

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def base_ret(fg, bg):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }

def separator_ret(color_d):
    return widget.Sep(**base_ret('text',color_d), linewidth=0, padding=5)

def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)



def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces():
    return [
        separator(),
        separator(),
        widget.TextBox(text=' ', foreground='#ff0000', background=colors['dark'],fontsize=21, mouse_callbacks={'Button1': Apps_rofi}),
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=19,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator_ret('dark'),

    powerline('color4', 'dark'),

    icon(bg="color4", text=' '), # Icon: nf-fa-download
    separator_ret('color4'),

    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

    #icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.TextBox(text=' ', background=colors['color3'], fontsize=19, mouse_callbacks={'Button1': Wifi_rofi}),
    widget.Net(**base(bg='color3'), interface='wlp2s0'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    #widget.TextBox(text='墳 ', background=colors['color1'], fontsize=19),
    widget.Volume(background=colors['color1'], channel='Master', device='default', emoji=True, theme_path='/home/leocarrillo/.config/qtile/volume-icons'),
    #widget.TextBox(text=' ', background=colors['color1'], fontsize=19),
    #widget.Battery(background=colors['color1'], charge_char=' ', discharge_char=' ',empty_char=' ',full_char=' '),
    #widget.BatteryIcon(background=colors['color1'], theme_path='/home/leocarrillo/.config/qtile/battery-icons'),
    #widget.TextBox(text='Hola',background=colors['color4'], mouse_callbacks={'Button1': nautilus_ex1}),

    #powerline('dark', 'color1'),

    widget.Systray(background=colors['color1'], padding=5),

    #icon(bg="color1", fontsize=17, text=' '),
    #widget.Wlan(**base(bg='color3'), interface='wlan0'),

    powerline('color1', 'color1'),
    powerline('color4', 'color1'),
    separator_ret('color4'),
    separator_ret('color4'),
    widget.TextBox(background=colors['color4'], foreground='#ff0000' , text=' ',fontsize=19, mouse_callbacks={'Button1': Power_rofi}),
    separator_ret('color4'),
    separator_ret('color4'),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

# widget_defaults = dict(
#     font='Cantarell',
#     fontsize=16,
#     padding=3,
# )

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}

extension_defaults = widget_defaults.copy()

# widget_defaults = dict(
#     font='Cantarell',
#     fontsize=16,
#     padding=3,
# )
# extension_defaults = widget_defaults.copy()

def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.75)


screens = [
    Screen(
        top=status_bar(primary_widgets
        ))]

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    connected_monitors = int(command.stdout.decode("UTF-8"))

if connected_monitors > 1:
    for _ in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))

# screens = [
#     Screen(
#         top=bar.Bar(
#             [
#                 widget.CurrentLayoutIcon(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         'launch': ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 #widget.TextBox("default config", name="default"),
#                 #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                 widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
# 		widget.Systray(),
#                 widget.QuickExit(),
#             ],
#             30,
# 	    background="#222222",
# 	    opacity=0.8
#         ),
#     ),
# ]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

auto_fullscreen = True
focus_on_window_activation = "urgent"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# autostart = [
#     "setxkbmap us",
#     "feh --bg-fill /home/leocarrillo/Pictures/'Crazytut0s (4).png'",
# 	"nm-applet &",
# 	"blueman-applet &",
# 	"nautilus &",
# 	"Alacritty &",
#     "cbatticon &",
#     "volumeicon &",
# ]

# for x in autostart:
#     os.system(x)
