# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz funkcję ping, która będzie mogła wykonać polecenie systemowe ping w celu sprawdzenia osiągalności adresu hosta przekazanego jako parametr funkcji.

"""
import subprocess


def ping(url:str):
    proc = subprocess.Popen(args=['ping -c 2 {url}'.format(url=url)], stdout=subprocess.PIPE, shell=True)
    return proc.communicate()

if __name__ == '__main__':
    print(ping('wp.pl')[0])