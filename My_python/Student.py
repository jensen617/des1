# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:54:04 2022

@author: 20716
"""

class Student():
    def __init__(self,name):
        self._name=name
        self._subject_list=[]
    def add_subject(self,subject_name):
        self._subject_list.append(subject_name)
    def get_student_data(self):
        print(f'Student:{self._name} is assigned to:')
        for subject in self._subject_list:
            print(f'{subject}')
        print()