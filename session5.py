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
    print(table)
    
if __name__ == '__main__': 
    main()