# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 12:24:32 2020

@author: aryav
"""
import time 
dic={0:1,1:1}
def fib(n):
    if n in dic:
        return dic[n]
    else:
        dic[n]=fib(n-1)+fib(n-2)
        return dic[n]
start=time.time()
print(fib(2956))
print()
print(time.time()-start)
