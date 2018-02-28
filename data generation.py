# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:32:22 2018

@author: Admin
"""

import random

# save your csv file at the location mentioned
file=open('C:\\Users\\Admin\\Desktop\\Human Resource Analytics\\FinalData.csv',"w")

# Categorical Attirbutes 
Department=["sales","accounting","hr","technical","support","IT","product_mng" ]
Salary=["low","medium","high"]


for i in range (100000) : # number of Rows = 100000
   line=str(random.random())+";"+str(random.random())+";"+str(random.randint(1,10))+";"+str(random.randint(100,500))+";"+str(random.randint(1,10))+";"+str(random.randint(0,1))+";"+str(random.randint(0,1))+";"+str(random.randint(0,1))+";"+str(Department[random.randint(0,6)])+";"+str(Salary[random.randint(0,2)])+"\n"
   file.write(line)
   print ("\t"+line)
file.close()

