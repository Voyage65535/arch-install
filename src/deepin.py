#!/usr/bin/env python

from src import inst_conf, pacman
from sh  import sed, gsettings, systemctl


def dde():
    pacman(S='xorg', _in='\n\ny')
    pacman('-S', 'noto-fonts', 'noto-fonts-cjk', 'noto-fonts-emoji', 'otf-fira-mono', 'powerline-fonts', _in='y')
    pacman('-S', 'deepin', 'deepin-extra', _in='\n\n\ny')

def vbox():
    pacman(S='virtualbox-guest-modules-arch virtualbox-guest-utils', _in='y')
    systemctl('enable', 'vboxservice')

def deconf():
    pacman(S='xorg-xinit', _in='y')
    pacman(S='numlockx', _in='y')
    pacman('-S', 'fcitx-im', 'fcitx-configtool', 'fcitx-sogoupinyin', 'fcitx-table-other', _in='\ny')
    inst_conf('/', 'xinitrc')
    inst_conf('~', 'profile')

def ddeconf():
    inst_conf('~', 'locale.conf')
    inst_conf('~', 'config.conf')

def prvconf():
    inst_conf('~', 'user')

if __name__ == '__main__':
    dde()
    deconf()
    ddeconf()
    prvconf()

