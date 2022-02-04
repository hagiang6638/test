# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:23:48 2022

@author: HP
"""

# Tính và in ra phần nguyên, phần dư của phép chia 2 số nguyên a,b
a = int(input("Nhập a = "))
b = int(input("Nhập b = "))

print("Phép chia phần nguyên của 2 số nguyên {0}, {1}: ".format(a, b))
print("{0} // {1} = {2}".format(a, b, a//b))

print("Phép chia phần dư của 2 số nguyên {0}, {1}: ".format(a, b))
print("{0} % {1} = {2}".format(a, b, a%b))

