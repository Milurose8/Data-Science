#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:34:49 2021

@author: sjcet
"""

#6. Write a program to find out the value of X using solve(), given A and b as above
import numpy as np
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
b=np.array([[3],
             [5],
             [-2]])
inv=np.linalg.inv(A)
x=np.linalg.solve(inv,b)
print(x)