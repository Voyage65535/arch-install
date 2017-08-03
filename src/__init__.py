from os        import makedirs
from os.path   import exists
from shutil    import copy
from sh        import Command
from sys       import stdout, stderr, modules
from types     import ModuleType
from functools import wraps, partial


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
    data = 'data/'
    path = _conf[prefix] + _conf[name]

    if not exists(path):
        makedirs(path)
    copy(data + _conf[name], path)


# Some sh calls need all stdout and stderr to output
def _full_output(f):
    @wraps(f)
    def g(*args, **kwargs):
        kwargs['_out'] = stdout
        kwargs['_err'] = stderr
        return f(*args, **kwargs)
    return g


# Use stub to equip the decorator
@_full_output
def _stub(name, *args, **kwargs):
    return Command(name)(*args, **kwargs)


# Get the non-existent symbol reference,
# then use Command() to generate callable
class _cmd_generator(ModuleType):

    def __init__(self, modules):
        self.self_modules = modules

    def __getattr__(self, item):
        return partial(_stub, item)

if __name__ != '__main__':
    self = modules[__name__]
    modules[__name__] = _cmd_generator(self)
