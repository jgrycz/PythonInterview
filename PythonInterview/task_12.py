# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Znajdz wszystkie procesy mające czterocyfrowy PID znajdujące się w pliku proc_dump.txt. W tym celu użyj wyrażeń regularnych.

"""

import re

regex = '.* [0-9]4 [0-9]+ .*'