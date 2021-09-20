from functools import wraps
from time import sleep

def emphasized(function):
    @wraps(function)
    def wrappers(*args, **kwargs):

        return_val_from_undecorated = function(*args, **kwargs)

        emphasize = return_val_from_undecorated.upper() + "!"

        return emphasize

    return wrappers

def sarcastic(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        origenal_value = func(*args, **kwargs)
        return f'yes, "{origenal_value}" nice one'

    return wrappers


def proclaimes(func):
    @wraps(func)
    def wrappers(*args, **kwargs):
        origenal_value = func(*args, **kwargs)
        return "what i like do , " + origenal_value

    return wrappers

def procrastinates(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)

    return wrapper


@procrastinates
@proclaimes
def say(string):
    return string

@sarcastic
@emphasized
def suggestion(cuisines):
    return cuisines

if __name__ == "__main__":
    print(say('play football.'))