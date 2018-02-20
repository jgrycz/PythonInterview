# -*- coding: utf-8 -*-
"""
:author: Jaroslaw Grycz
:contact: jaroslaw.grycz@gmail.com
"""

import unittest

from PythonInterview.PythonInterview.task_05 import ProcParser


class TestProcParser(unittest.TestCase):
    def __init__(self):
        self.procTest = ProcParser('test_dump.txt')
        super().__init__()

    def test_load_data(self):
        self.procTest.load_data()
        self.assertIsNotNone(self.procTest.loaded_data)
        self.assertIsInstance(self.procTest.data, str)


    def test_user_procs(self):
        self.procTest.get_user_procs('root')
        self.assertIsNotNone(self.procTest.data)
        self.assertIsInstance(self.procTest.data, list)

if __name__ == '__main__':
    unittest.main()

