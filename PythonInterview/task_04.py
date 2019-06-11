# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz dekorator który będzie wypisywał na STDOUT nazwe wywołanej funkcji.

"""
from functools import wraps


def func_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapper


@func_name
def add(a, b):
    """Add!"""
    return a + b


add(2, 2)


@func_name
def dif(a, b):
    return a - b


dif(2019, add(2, 2))