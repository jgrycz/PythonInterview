# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Plik proc_dump.txt zawiera output z komendy ps -efw.
Dopisz metodę:
 - Która przeczyta plik ze wszystkimi procesami
 - Zwróci liste procesów należących do zadanego uzytkowinika

"""


class ProcParser:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def load_data(self):
        # TODO mehtod loads data from file self.output_file_path
        with open(self.output_file_path) as f:
            self.loaded_data = f.read()

    def get_user_procs(self, user):
        proccesses = self.loaded_data.split('\n')
        self.data = [i for i in proccesses if user in i.split(' ')[0]]


if __name__ == '__main__':
    boo = ProcParser('proc_dump.txt')
    boo.load_data()
    print(type(boo.loaded_data))
    boo.get_user_procs('root')
    print("\n".join(boo.data))