# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz powtarzające się elementy w zbiorach x oraz y.

"""

# 1
x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 5, 7]

duplicates = set(x).intersection(set(y))
# 2
x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
y = {'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

duplicates = {i: x[i] for i in x if i in y}
# 3 set 1


# 4 set 2

# 5 () a []
duplicates = set(x).intersection(set(y))

# 6
# Notacja duże O

# l = [1, 2, 3]
# O( 4 in l )

# d = {'a': 1, 'b': 2, 'c': 3'}
# O( d['a'] )
