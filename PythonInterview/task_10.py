# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Funkcja countdown odlicza do zera, uruchom tę funkcję w 3 różnych wątkach.

"""
import time
from threading import Thread


def countdown(description, n):
    while n > 0:
        print(description, n)
        n -= 1
        time.sleep(1)


threads = []
for i in range(1, 4):
    Thread(target=countdown,
           args=(f'thread no {i}', 10)).start()
