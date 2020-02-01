#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:42:52 2019

@author: naotto
"""
import random as rnd, numpy as np

def evaluate(x):
    return np.sin(np.pi*x/256)

def perturb(c):
    return c + 1

def hill_climbing(max_it, g):
    x = rnd.randint(0,255)
    x_eval = evaluate(x)
    t = 1
    while t < max_it and x_eval != g:
        x2 = perturb(x)
        x2_eval = evaluate(x2)
        print('x=',x)
        print('x2=',x2)
        if x2_eval > x_eval:
            x = x2
        t +=1
        print('t=',t)
        print('_______________________')

