#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:53:59 2026

@author: charlotte
"""

def add(x, y):
    x = float(x)
    y = float(y)
    sum = x + y
    print(f'\nThe sum of {x} and {y} is {sum}.\nThe type of the sum is {type(sum)}\n')
    
def subtract(x, y):
    x = int(x)
    y = int(y)
    difference = x - y
    print(f'\nThe difference of {x} and {y} is {difference}.\nThe type of the difference is {type(difference)}\n')
    
def multiply(x, y):
    x = float(x)
    y = int(y)
    product = x * y
    print(f'\nThe product of {x} and {y} is {product}.\n The type of the product is {type(product)}\n')
    





def main():
    x = input("What is the first number?\n")
    y = input("What is the second number?\n")
    add(x, y)
    subtract(x, y)
    multiply(x, y)
    
    
    
if __name__ == "__main__":
    main()