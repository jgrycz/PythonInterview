# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz funkcję ping, która będzie mogła wykonać polecenie systemowe ping w celu sprawdzenia osiągalności adresu hosta przekazanego jako parametr funkcji.

"""
from subprocess import check_call


def ping(host):
    return check_call(["ping", "-c", "1", host]) == 0

try:
    ping("localhost")
except OSError as w:
    print(w)
except (AttributeError, BufferError) as w:
    print(w)

