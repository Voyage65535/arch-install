#!/usr/bin/env python

import src
from os import system
from os.path import expanduser
from shutil import copy
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
    pacman('-S', 'fcitx-im', 'fcitx-configtool', 'fcitx-sunpinyin', 'fcitx-mozc', 'fcitx-table-other', _in='\ny', _out=stdout, _err=stderr)
    copy(src.xinitrc, '/etc/X11/xinit/xinitrc')

def ddeconf():
    copy(src.locale, expanduser('~/.config/locale.conf'))
    copy(src.termconf, expanduser('~/.config/deepin/deepin-terminal/config.conf'))

def prvconf():
    copy(src.audio, expanduser('~/.config/deepin/dde-daemon/audio.json'))
    gsettings('set', 'com.deepin.dde.keybinding.system', 'terminal', "['<Super>B']")

if __name__ == '__main__':
    dde()
    deconf()
    ddeconf()
    prvconf()

