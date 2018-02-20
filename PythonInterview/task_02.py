# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz powtarzające się elementy w zbiorach x oraz y.

"""

# 1
x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 5, 7]

print(set(x).intersection(set(y)))

# 2
x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
y = {'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

print(
    [item for item in x.items() if item in y.items()]
)

# 3 set 1


# 4 set 2

# 5 () a []

# 6
# Notacja duże O

# l = [1, 2, 3]
# O( 4 in l )
# n
# d = {'a': 1, 'b': 2, 'c': 3'}
# O( d['a'] )
# (n)
