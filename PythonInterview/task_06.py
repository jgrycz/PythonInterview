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
from contextlib import contextmanager


class ProcParser:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def load_data(self):
        with open(self.output_file_path) as f:
            self.loaded_data = f.read()

    def get_user_procs(self, user):
        proccesses = self.loaded_data.split('\n')
        self.data = [i for i in proccesses if user in i.split(' ')[0]]
        return self.data


@contextmanager
def setup_parser(file_path):
    #ENTER
    x = ProcParser(file_path)
    x.load_data()
    yield x

    #EXIT

if __name__ == '__main__':
    file_path = 'proc_dump.txt'
    with setup_parser(file_path) as pp:
        print(pp.get_user_procs('pi'))

