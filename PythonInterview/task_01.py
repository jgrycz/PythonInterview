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
    tree_width = n//2+1
    for i in range(n):
        out += ' ' * (tree_width - i) + '*'* (1 + 2*i ) + '\n'
    else:
        out += tree_width * ' ' + '|'

    return out


if __name__ == '__main__':
    print(print_tree(5))