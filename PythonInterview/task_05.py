# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com

Plik proc_dump.txt zawiera output z komendy ps -efw.
Dopisz funkcje:
 - Która przeczyta plik ze wszystkimi procesami
 - Zwróci liste procesów należących do zadanego uzytkowinika

"""


class ProcParser:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def load_data(self):
        # TODO mehtod loads data from file self.output_file_path
        pass

    def get_user_procs(self, user):
        # TODO returns all procs owned by user
        pass
