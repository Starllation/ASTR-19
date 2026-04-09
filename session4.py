#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:56:33 2026

@author: charlotte
"""

class animal:
    def __init__(self, arm, leg, num_eyes, tail, furry):
        self.arm = float(arm)
        self.leg = float(leg)
        self.num_eyes = int(num_eyes)
        self.tail = bool(tail)
        self.furry = bool(furry)
        
    def __str__(self):
        return f'''The animal has arms that are length {self.arm} and legs that are {self.leg}. 
It has {self.num_eyes} eyes. It {'does' if self.tail == True else 'does not'} have a tail and it {'is' if self.furry == True else 'is not'} furry.'''
        

def main():
   fox = animal(10.5, 12, 2, True, True)
   print('''I'm not sure how long a fox's arms and legs are. I will use 10.5 and 12.''')
   print(fox)
    
if __name__ == "__main__":
    main()
