# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Załóż, że funkcja raise_exception jest bardzo podatna na błędy, przez co może rzucić różne typy wyjątków.
Do obsługi wyjątków została napisana specjalna klasa (ExceptionHandler) potrafiąca przywrócić poprawny stan aplikacji.

Napisz taki dekorator który w razie awarii zapewni dalsze działanie aplikacji.

"""
from random import choice


class handler_decorator:
    def __init__(self, foo, exceptions):
        self.foo = foo
        self.exceptions_and_handlers = [IOError, ImportError, EnvironmentError, Exception, BaseException]

    def __call__(self, *args, **kwargs):
        def wrapper():
            try:
                return self.foo(*args)
            except Exception as e:
                print(e)

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
