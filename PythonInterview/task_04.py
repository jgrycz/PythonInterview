# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz dekorator który będzie wypisywał na STDOUT nazwe wywołanej funkcji.

"""
from functools import wraps
import typing


def some_decorator(f: typing.Callable):
    @wraps(f)
    def foo(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return foo


@some_decorator
def some_function(x: int) -> int:
    return x*x


if __name__ == '__main__':
    print(some_function(5))
