# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Zaimplementuj wzorzec Singleton

"""


class SinglePy:
    class __SinglePy:
        def __init__(self, x):
            self.x = x

        def __str__(self):
            return repr(self) + self.x
    instance = None

    def __init__(self, x):
        if not SinglePy.instance:
            SinglePy.instance = SinglePy.__SinglePy(x)
        else:
            SinglePy.instance.x = x

