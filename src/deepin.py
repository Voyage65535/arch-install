#!/usr/bin/env python

from os import system
from os.path import expanduser
from sys import stdout, stderr
from sh import pacman, sed, gsettings

def dde():
    pacman(S='xorg', _in='\n\ny', _out=stdout, _err=stderr)
    pacman(R='xf86-video-vesa', _in='y', _out=stdout, _err=stderr)
    driv = input('Input your video driver (e.g. xf86-video-intel): ')
    pacman(S=driv, _in='y', _out=stdout, _err=stderr)

    pacman('-S', 'noto-fonts', 'noto-fonts-cjk', 'otf-fira-mono', 'powerline-fonts', _in='y', _out=stdout, _err=stderr)
    pacman('-S', 'deepin', 'deepin-extra', _in='\n\n\ny', _out=stdout, _err=stderr)

def deconf():
    pacman(S='xorg-xinit', _in='y', _out=stdout, _err=stderr)
    pacman(S='numlockx', _in='y', _out=stdout, _err=stderr)
    pacman('-S', 'fcitx-im', 'fcitx-configtool', 'fcitx-sogoupinyin', 'fcitx-mozc', 'fcitx-table-other', _in='\ny', _out=stdout, _err=stderr)
    xinitrc = '/etc/X11/xinit/xinitrc'

    sed('/twm &/d', i=xinitrc)
    sed('/xclock -geometry 50x50-1+1 &/d', i=xinitrc)
    sed('/xterm -geometry 80x50+494+51 &/d', i=xinitrc)
    sed('/xterm -geometry 80x20+494-0 &/d', i=xinitrc)
    sed('/exec xterm -geometry 80x66+0+0 -name login/d', i=xinitrc)

    f = open(xinitrc, 'a')
    xinitrc = '''
export LANG=zh_CN.UTF-8
export XMIDIFIERS=@im=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx

setxkbmap -option caps:swapescape
numlockx &
startdde

    '''
    f.write(xinitrc)
    f.close

def ddeconf():
    termconf = '''
[general]
theme=argonaut
opacity=0.85
font=Fira Code
font_size=12

[shortcut]
copy=Ctrl + Shift + c
paste=Ctrl + Shift + v
open=Ctrl + Shift + x
search=Ctrl + Shift + f
zoom_in=Ctrl + =
zoom_out=Ctrl + -
default_size=Ctrl + 0
select_all=Ctrl + Shift + a
jump_to_next_command=Shift + Down
jump_to_previous_command=Shift + Up
new_workspace=Ctrl + Shift + t
close_workspace=Ctrl + Shift + w
next_workspace=Ctrl + Tab
previous_workspace=Ctrl + Shift + Tab
vertical_split=Ctrl + Shift + j
horizontal_split=Ctrl + Shift + h
select_upper_window=Alt + k
select_lower_window=Alt + j
select_left_window=Alt + h
select_right_window=Alt + l
close_window=Ctrl + Alt + q
close_other_windows=Ctrl + Shift + q
switch_fullscreen=F11
display_shortcuts=Ctrl + Shift + ?
custom_commands=Ctrl + [
remote_management=Ctrl + /
select_workspace=Alt

[advanced]
cursor_shape=block
cursor_blink_mode=true
scroll_on_key=true
scroll_on_output=false
scroll_line=-1
use_on_starting=window
window_width=0
window_height=0
quake_window_height=0
remote_commands=zssh
hide_quakewindow_after_lost_focus=false
show_quakewindow_tab=true
follow_active_window=true

[theme]
color_1=#232323
color_2=#ff000f
color_3=#8ce10b
color_4=#ffb900
color_5=#008df8
color_6=#6d43a6
color_7=#00d8eb
color_8=#ffffff
color_9=#444444
color_10=#ff2740
color_11=#abe15b
color_12=#ffd242
color_13=#0092ff
color_14=#9a5feb
color_15=#67fff0
color_16=#ffffff
background=#0e1019
foreground=#fffaf4
tab=#f2f2f2
style=dark

'''
    f = open(expanduser('~/.config/deepin/deepin-terminal/config.conf'), 'w')
    f.write(termconf)
    f.close()

def prvconf():
    audio = '''
{
    "Profiles":{
        "alsa_card.pci-0000_00_14.2":"output:analog-stereo+input:analog-stereo",
        "alsa_card.pci-0000_01_00.1":"output:hdmi-stereo"
    },
    "Sink":"alsa_output.pci-0000_01_00.1.hdmi-stereo",
    "Source":"alsa_input.pci-0000_00_14.2.analog.stereo",
    "SinkPort":"hdmi-output-0",
    "SourcePort":"analog-input-front-mic",
    "SinkVolume":1,
    "SourceVolume":0.25
}

'''
    f = open(expanduser('~/.config/deepin/dde-daemon/audio.json'), 'w')
    f.write(audio)
    f.close()

    gsettings('set', 'com.deepin.dde.keybinding.system', 'terminal', "['<Super>B']")

if __name__ == '__main__':
    dde()
    deconf()
    #ddeconf()
    #prvconf()

