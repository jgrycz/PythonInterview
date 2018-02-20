# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com
"""

# 1 Wypakuj poniższą tuple tak aby, odrzucić elementy skrajne czyli aby nowa typla składała się tylko z elementów: 'Grycz' i 'Rozmowa'
t = ('Jarek', 'Grycz', 'Rozmowa', 'Kwalifikacyjna')
nt = t[1:-1]
print(nt)

# 2 Z poniższego stringa utwórz nowy ciąg znaków w którego skład wejdzie co drugi znak z bazowego ciągu znaków
# 'Jakis losowy napis' => 'Jkslsw ai'
s = 'Jakis losowy napis'
print(s[::2])