# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Plik proc_dump.txt zawiera output z komendy ps -efw.
Dopisz funkcje:
 - Która przeczyta plik ze wszystkimi procesami
 - Zwróci liste procesów należących do zadanego uzytkowinika

"""
from contextlib import contextmanager


@contextmanager
def setup_parser(path):
    yield ProcParser(path)


class ProcParser:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass

    def load_data(self):
        # TODO mehtod loads data from file self.output_file_path
        with open(self.output_file_path, 'r') as file:
            return file.read()

    def get_user_procs(self, user):
        # TODO returns all procs owned by user

        # return (line for line in self.load_data().split('\n') if user == line.split()[0])
        for line in self.load_data().split('\n'):
            if user == line.split()[0]:
                yield line


if __name__ == '__main__':
    import pdb; pdb.set_trace()
    from pprint import pprint
    pp = ProcParser('proc_dump.txt')
    pprint(pp.get_user_procs('root'))
    with ProcParser('proc_dump.txt') as pp:
        pprint(pp.get_user_procs('root'))

    with setup_parser('proc_dump.txt') as pp:
        pprint(pp.get_user_procs('root'))
