#!/usr/bin/env python
"""
"""
import functools

def lower_if_string(x):
    if isinstance(x, basestring):
        x = x.lower()
    else:
        raise TypeError("%s is not a string")
    return x

def check_querytable_inputs(fn):
    """Check the arguments to the Query.__init__ function
    """
    args = ['query',]

    @functools.wraps(fn)
    def wrapped(*args, **kwargs):
        args = map(lower_if_string, args)
        kwargs = dict((k, lower_if_string(v)) for k, v in kwargs.iteritems())
        return fn(*args, **kwargs)
    return wrapped







if __name__ == '__main__':
    pass

