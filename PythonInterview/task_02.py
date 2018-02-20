# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz powtarzające się elementy w zbiorach x oraz y.

"""

# 1
#
#
# # 2
# x = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 686}
# y = {'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
#
# repeat_dict = {k: x[k] for k in x.keys() if k in y.keys() and x[k] in y.values()}
# print(repeat_dict)
# 3 set 1
# x = {i for i in range(4)}
# y = {i for i in range(3, 10)}
#
# print(x.intersection(y))

# 4 set 2


# 5 () a []
x = [1, 2, 3, 4, 5]
y = [3, 4, 5, 5, 7]
repeat = (int(i) for i in x if i in x and i in set(y))
print([*repeat])

# 6
# Notacja duże O

# l = [1, 2, 3]
# O( 4 in l )
"""
O(n)
"""

# d = {'a': 1, 'b': 2, 'c': 3'}
# O( d['a'] )
"""
O(long(n))
"""
