#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: array_read_write.py
#Feature:
#Author: kernellmd 
#Created Time: 2018-10-02 20:59:43
############################  

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print("floats[-1] = {}".format(floats[-1]))
with open('floats.bin', 'wb') as f:
    floats.tofile(f)

floats2 = array('d')
with open('floats.bin', 'rb') as f:
    floats2.fromfile(f, 10**7)
print("floats2[-1] = {}".format(floats2[-1]))

print("'floats == floats2' is {}".format(floats2 == floats))

