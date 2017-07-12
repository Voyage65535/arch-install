from os import makedirs
from shutil import copy

github_raw = "https://raw.githubusercontent.com/"

_colormake='pagekite/colormake/master/'
color = {
    '/usr/bin/colormake.pl':github_raw+_colormake+'colormake.pl',
    '/usr/bin/colormake':github_raw+_colormake+'colormake',
    '/usr/bin/clmake':github_raw+_colormake+'clmake',
    '/usr/bin/prettyping':github_raw+'denilsonsa/prettyping/master/prettyping'
}

_conf = {
    'audio.json':'.config/deepin/dde-daemon/',
    'config.conf':'.config/deepin/deepin-terminal/',
    'env.ini':'.config/SogouPY/',
    'locale.conf':'.config/',
    'pacman.conf':'etc/',
    'profile':'.config/fcitx/'
    'xinitrc':'etc/X11/xinitrc/',
    '.zshrc':''
}
def home(name):
    data = 'data/'
    prefix = '/root/'
    makedirs(prefix+_conf[name])
    copy(data+_conf[name]+name, prefix+_conf[name])
def root(name):
    data = 'data/'
    prefix = '/'
    makedirs(prefix+_conf[nam])
    copy(data+_conf[name]+name, prefix+_conf[name])

