# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

W klasie ProcParser zrób refactoring metody get_user_procs tak aby ta metoda stała się generatorem.

"""

class ProcParser:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def load_data(self):
        with open(self.output_file_path) as f:
            self.loaded_data = f.read()

    def get_user_procs(self, user):
        proccesses = self.loaded_data.split('\n')
        for i in proccesses:
            if user in i.split(' ')[0]:
                yield i


if __name__ == '__main__':
    boo = ProcParser('proc_dump.txt')
    boo.load_data()
    boo.get_user_procs('root').__next__()
    boo.get_user_procs('root').__next__()
    boo.get_user_procs('root').__next__()
    boo.get_user_procs('root').__next__()
    boo.get_user_procs('root').__next__()
    boo.get_user_procs('root').__next__()
    print(type(ProcParser.get_user_procs))

