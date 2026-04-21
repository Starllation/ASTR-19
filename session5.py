#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:11:39 2026

@author: charlotte
"""

import numpy as np
import math
from astropy.table import Table 


def main(): 
    x = np.linspace(0, 2*math.pi, 1000)
    sin = np.sin(x)
    table = Table([x, sin], names=['x', 'sin(x)'])
    while True:
        answer = input('1 to see all 1000 rows. 0 to see condensed version.\n')
        if answer == '1':
            table.pprint(max_lines = -1)
            break
        elif answer == '0':
            print(table)
            break
    
    
if __name__ == '__main__': 
    main()