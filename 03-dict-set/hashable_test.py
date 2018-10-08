#!/usr/bin/env python3
#-*- coding: utf-8 -*-  
############################  
#File Name: hashable_test.py
#Feature:
#Author: kernellmd 
#Created Time: 2018-10-08 10:21:17
############################  

#只有当一个元组所包含的所有元素都是可散列的情况下，它才是可散列的

tt = (1, 2, (30, 40))
print(hash(tt))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

tl = (1, 2, [30, 40])
print(hash(tl))
