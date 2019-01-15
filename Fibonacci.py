# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 22:31:35 2019

@author: Yenis
"""

n=15
def fibonacci(n):
    f0 = 0
    f1 = 1
    f = [1] * n
    for i in range (1,n):
        f[i] = f0 + f1
        f0, f1 = f1, f[i]
    return f
print(fibonacci(n))