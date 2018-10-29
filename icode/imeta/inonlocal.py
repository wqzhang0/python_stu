from functools import wraps, partial
import logging
# Utility decorator to attach a function as an attribute of obj
from icode.imeta.iwraps import timethis


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    '''
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        @attach_wrapper(wrapper)
        def get_level():
            return level

        return wrapper

    return decorate

# Example use
@timethis
@logged(logging.DEBUG)
def add(x, y):
    return x + y
@timethis
@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

logging.basicConfig(level=logging.DEBUG)

add(2, 3)

add.set_message('Add called')
add(2, 3)

add.set_level(logging.WARNING)
print(add.get_level())
add(2, 3)