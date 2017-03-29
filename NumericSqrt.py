# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:04:40 2017

@author: julien

Numeric clalculations of sqrt
-----------------------------
n: number to calculate the square root
iter: number of iterations
plot: plot convergence

--- usage (to calculate the square root of 2) ---
 % only calculate the square root of 2
 n = nestedIntervalSqrt(2)
 % 100 iterations and plot the convergence
 n = herosMethodSqrt(2, iter=100, plot=True)
 
use %matplotlip qt to create an own window for the plot
"""

import numpy as np
import matplotlib.pyplot as plt

def nestedIntervalSqrt(n, iter=10, plot=False):
    a = [1]
    b = [n]
    for i in range(iter):
        c = (a[-1]+b[-1])/2.0 
        a.append(a[-1] if c*c > 2 else c)
        b.append(b[-1] if c*c <= 2 else c)
    if plot:
        drawSqrt(n,a,b)
    return (a[-1]+b[-1])/2.0

def heronsMethodSqrt(n, iter=10, plot=False):
    a = [1]
    for i in range(iter):
        a.append(0.5*(a[-1]+n/a[-1]))
    if plot:
        drawSqrt(n,a)
    return a[-1]
        
def drawSqrt(n,a,b=None):
    const = [np.sqrt(n) for i in range(len(a))]
    if b == None:    
        plt.plot(range(len(a)),const,
             range(len(a)), a, "--y")  
    else:
        plt.plot(range(len(a)),const,
                 range(len(a)), a, "--y",
                 range(len(b)), b, "--g")
    plt.show()
    
