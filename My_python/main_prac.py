# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:00:08 2022

@author: 20716
"""

from class import Student
from class import Dog
from class import Restaurant

student1=Student('Martin')
student1.add_subject('biomechanics_2020')
student1.get_student_data()

        
my_dog=Dog('Willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

restaurant_1=Restaurant('SanQiu Barbecue','buffet barbecue')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()