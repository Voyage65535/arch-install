from os        import makedirs
from os.path   import exists
from shutil    import copy


github_raw = "https://raw.github.com/"

_colormake='pagekite/colormake/master/'
color = {
    '/usr/bin/colormake.pl' : github_raw + _colormake + 'colormake.pl',
    '/usr/bin/colormake'    : github_raw + _colormake + 'colormake',
    '/usr/bin/clmake'       : github_raw + _colormake + 'clmake',
    '/usr/bin/prettyping'   : github_raw + 'denilsonsa/prettyping/master/prettyping'
}

_conf = {
    # prefix
    '~'           : '/root/',
    '/'           : '/',
    # path
    'config.conf' : '.config/deepin/deepin-terminal/',
    'locale.conf' : '.config/',
    'pacman.conf' : 'etc/',
    'profile'     : '.config/fcitx/',
    'user'        : '.config/dconf/',
    'xinitrc'     : 'etc/X11/xinit/',
    '.zshrc'      : ''
}


def inst_conf(prefix, name):
    data = '../data/'
    path = _conf[prefix] + _conf[name]

    if not exists(path):
        makedirs(path)
    copy(data + _conf[name] + name, path)

