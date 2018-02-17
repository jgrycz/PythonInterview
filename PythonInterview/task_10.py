# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Funkcja countdown odlicza do zera, uruchom tę funkcję w 3 różnych wątkach.

"""
import time


def countdown(description, n):
    while n > 0:
        print(description, n)
        n -= 1
        time.sleep(1)
