from os import makedirs
from os.path import exists
from shutil import copy

github_raw = "https://raw.github.com/"

_colormake='pagekite/colormake/master/'
color = {
    '/usr/bin/colormake.pl':github_raw+_colormake+'colormake.pl',
    '/usr/bin/colormake':github_raw+_colormake+'colormake',
    '/usr/bin/clmake':github_raw+_colormake+'clmake',
    '/usr/bin/prettyping':github_raw+'denilsonsa/prettyping/master/prettyping'
}

_conf = {
    'config.conf':'.config/deepin/deepin-terminal/',
    'locale.conf':'.config/',
    'pacman.conf':'etc/',
    'profile':'.config/fcitx/',
    'user':'.config/dconf/'
    'xinitrc':'etc/X11/xinit/',
    '.zshrc':''
}
def home(name):
    data = 'data/'
    prefix = '/root/'
    if not exists(prefix+_conf[name]):
        makedirs(prefix+_conf[name])
    copy(data+_conf[name]+name, prefix+_conf[name])
def root(name):
    data = 'data/'
    prefix = '/'
    if not exists(prefix+_conf[name]):
        makedirs(prefix+_conf[name])
    copy(data+_conf[name]+name, prefix+_conf[name])

