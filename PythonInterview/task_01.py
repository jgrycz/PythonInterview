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

def draw_tree(height):
    for i in range(height+1):
        print(' '*((height - i)//2), '*'*i)


if __name__ == '__main__':
    draw_tree(5)
