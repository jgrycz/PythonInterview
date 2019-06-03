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
    stars = -1
    for level in range(0, height):
        stars += 2
        print(" " * (height - level) + "*" * stars)
    else:
        full_width = 1 * (height - level) + 1 * stars
        print(" " * (full_width / 2) + "|")


if __name__ == "__main__":
    draw_tree(6)
    draw_tree(1)
    draw_tree(3)
    draw_tree(4)
