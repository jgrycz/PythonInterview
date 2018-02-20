# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Załóż, że funkcja raise_exception jest bardzo podatna na błędy, przez co może rzucić różne typy wyjątków.
Do obsługi wyjątków została napisana specjalna klasa (ExceptionHandler) potrafiąca przywrócić poprawny stan aplikacji.

Napisz taki dekorator który w razie awarii zapewni dalsze działanie aplikacji.

"""
from random import choice
from typing import Callable


def parse_exception(e: Exception):
    return 'Exception'


def cont(f: Callable):
    def wrapper():
        try:
            return f()
        except Exception as e:
            handler = ExceptionHandler()
            getattr(handler, f'handle_{parse_exception(e)}')()

        return wrapper()

def raise_exception():
    exceptions = [IOError, ImportError, EnvironmentError, Exception, BaseException]
    raise choice(exceptions)


class ExceptionHandler:
    def handle_IOError(self):
        pass

    def handle_ImportError(self):
        pass

    def handle_EnvironmentError(self):
        pass

    def handle_Exception(self):
        pass

    def handle_BaseException(self):
        pass


raise_exception()
