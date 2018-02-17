# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Do klasy ProcParser zaimplementuj funkcjonalność, która umożliwi pobranie procesów należących do roota'a w poniższy sposób:

with setup_parser(file_path) as pp:
    pp.get_user_procs('ROOT')

albo:

with ProcParser(file_path) as pp:
    pp.get_user_procs('ROOT')

"""
