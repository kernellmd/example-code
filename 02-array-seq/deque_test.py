#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: deque_test.py
#Feature:
#Author: kernellmd 
#Created Time: 2018-10-08 08:24:47
############################  

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)
