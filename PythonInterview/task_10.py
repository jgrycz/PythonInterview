# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Funkcja countdown odlicza do zera, uruchom tę funkcję w 3 różnych wątkach.

"""
import threading
import time


def countdown(description, n):
    while n > 0:
        print(description, n)
        n -= 1
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=countdown, args=('d1', 10)).start()
    time.sleep(1)
    threading.Thread(target=countdown, args=('d2', 10)).start()
    time.sleep(1)
    threading.Thread(target=countdown, args=('d3', 10)).start()
    time.sleep(1)

