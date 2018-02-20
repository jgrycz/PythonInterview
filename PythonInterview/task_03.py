# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com
"""

# 1 Wypakuj poniższą tuple tak aby, odrzucić elementy skrajne czyli aby nowa typla składała się tylko z elementów: 'Grycz' i 'Rozmowa'
t = ('Jarek', 'Grycz', 'Rozmowa', 'Kwalifikacyjna')
y = t[1:3]
y = (t[1], t[2])
_, grycz, rozmowa, _ = t
y = t[0], t[-1]
x, *_, y = t
print(x, y)

# 2 Z poniższego stringa utwórz nowy ciąg znaków w którego skład wejdzie co drugi znak z bazowego ciągu znaków
# 'Jakis losowy napis' => 'Jkslsw ai'
s = 'Jakis losowy napis'
