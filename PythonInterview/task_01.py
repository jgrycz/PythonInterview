# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Napisz funkcję rysującą choinkę, wysokość choinki ma być przekazana jako argument funkcji.

Choinka powinna wyglądać jak poniżej:

  *
 ***
*****
  |


"""


def print_tree(n: int):
    out = ''
    for i in range(n):
        out += ' ' * (n - i) + '*' * (i*2+1) + '\n'
    else:
        out += n * ' ' + '|'
    return out


if __name__ == '__main__':
    print(print_tree(16))
