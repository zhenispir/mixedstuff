# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:18:50 2019

@author: Yenis
"""

from vpython import *
def f(x):
    return (sin(x))**2*(cos(x))**2

def bisection(xminus,xplus,Nmax,eps):
    for it in range(0,Nmax):
        x = (xplus+xminus)/2
        print('it=', it, 'x=', x, 'f(x)=', f(x))
        if (f(xplus)*f(x)>0.):
            xplus=x
        else:
            xminus=x
        if (abs(f(x)) < eps):
            print('\n Root found with precision eps = ',eps)
            break
        if it == Nmax-1:
            print('\n Root NOT found after Nmax iterations\n')
    return x

eps = 1e-6
a = 0.0; b = 3.0
imax = 100
root = bisection(a, b, imax, eps)
print('Root = ', root)
