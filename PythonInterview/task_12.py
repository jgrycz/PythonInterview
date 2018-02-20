# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz wszystkie procesy mające czterocyfrowy PID znajdujące się w pliku proc_dump.txt. W tym celu użyj wyrażeń regularnych.

"""

import re


if __name__ == '__main__':
    with open('proc_dump.txt') as f:
        data = f.read()
    regex = re.compile('^[\w]+ *[0-9]{4} *[0-9]+ .*')
    out = [i for i in data.split('\n') if regex.match(i)]
    print("\n".join(out))
