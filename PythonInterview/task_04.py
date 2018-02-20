# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz dekorator który będzie wypisywał na STDOUT nazwe wywołanej funkcji.

"""


class test_decorator:
    def __init__(self, foo):
        self.foo = foo

    def __call__(self, *args, **kwargs):
        def wrapper():
            return self.foo(*args)
        print(self.foo.__name__, self.foo.__doc__)
        return wrapper()


@test_decorator
def bar(x, y):
    """
    :param x:
    :return:
    """
    return x**y


if __name__ == '__main__':
    static_y_bar = bar(y=2)
    static_y_bar(2)
    static_y_bar(5)
