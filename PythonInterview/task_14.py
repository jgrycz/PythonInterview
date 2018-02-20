# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Katalog syslogs zawiera kilka plików z logami, napisz funkcje która sprawdzi zawartość katalogu oraz złączy zawartość wszystkich plików w jeden, z nazwą zawierającą bieżącą date.
Funkcja ma działać niezależnie od platformy.

"""
import os


def merge_syslogs(path):
    x = os.path.abspath(path)
    syslogs_path = [f for f in os.listdir(x) if f.endswith('.log')]
    log_out = ''
    for log in syslogs_path:
        with open(os.path.join(x, log)) as f:
            log_out += f.read()

    
    return log_out


if __name__ == '__main__':
    merge_syslogs('./syslogs')