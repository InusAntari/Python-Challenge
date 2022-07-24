# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:18:24 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/map.html
'''

import string

szyfr = "map"

# slowa = szyfr.split(' ')

# define an alphabet
alfa = "abcdefghijklmnopqrstuvwxyz"
alfa2 = "cdefghijklmnopqrstuvwxyzab"
klucz = szyfr.maketrans(alfa, alfa2)

print(szyfr.translate(klucz))