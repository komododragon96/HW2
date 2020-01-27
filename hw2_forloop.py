#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 19:41:54 2020

@author: komodothedragon96
"""
from __future__ import print_function

x= [[0, 1, 2, 3,], [4, 5, 6, 7],[8, 9, 10, 11], [12, 13, 14, 15]]

for y in x:
    print(*y, sep='&')
