#!/usr/bin/env python
"""
"""

def test_decorator_tolowerstring():
    from decorators import slug_to_lower

    @slug_to_lower
    def print_lowercase(x):
        return x

    for xi in ['a', 'A', ' ', '331', 'aAAaa']:
        assert print_lowercase(xi) == xi.lower()
        print print_lowercase(xi)

    for xi in [1, 2]:
        print xi






if __name__ == '__main__':
    test_decorator_tolowerstring()

