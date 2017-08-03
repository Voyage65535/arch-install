from sh        import Command
from sys       import stdout, stderr, modules
from types     import ModuleType
from functools import wraps, partial


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
    print(__name__)
    self = modules[__name__]
    modules[__name__] = _cmd_generator(self)
