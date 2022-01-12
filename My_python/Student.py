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
        
class Dog:
    """模拟小狗的简单尝试"""
    def __init__(self,name,age):
        """初始化属性name和age"""
        self.name=name
        self.age=age
        
    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """模拟小狗收到命令时打滚。"""
        print(f"{self.name} rolled over!")
        
    