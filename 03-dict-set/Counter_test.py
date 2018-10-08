#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: Counter_test.py
#Feature:
#Author: kernellmd 
#Created Time: 2018-10-08 16:30:02
############################  

import collections

ct = collections.Counter('abracadabra')
print(ct)

ct.update('aaaaazzz')
print(ct)

#返回映射里最常见的n个键和他们的计数
print(ct.most_common(2))

