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
import re


def christmas_tree(n):
    """

    :param n:
    :return:
    """
    result = ""
    for i in range(n):
        line = (n - i) * " " + "*" * ((2*i - 1) + 2)
        print(line)


print(christmas_tree(4))


def test_christmas_tree():
    assert christmas_tree(0) == ""
    assert christmas_tree(1) == "*"
    assert christmas_tree(3) == "  *  \n *** \n*****"

s = "Nov 14 21:17:05 raspb err ypi kernel: [    0.000000]     fixmap  : 0xffc00000 - 0xfff00000   (3072 kB)"

pattern = re.compile(r"\s(\d{2}:\d{2}:\d{2})\s([a-zA-Z\s]+)\s")

print(pattern.findall(s))
