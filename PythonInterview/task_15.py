"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz wszystkie klasy nie będące podklasą klasy BaseClass.
"""
from abc import ABCMeta


class BaseClass(metaclass=ABCMeta):
    pass


class A(BaseClass):
    pass


class B:
    pass


class C(BaseClass):
    pass


class D:
    pass


class E(BaseClass):
    pass


classes = [A, B, C, D, E]
