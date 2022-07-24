# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 21:45:14 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/peak.html
'''

import requests
import bs4
import pickle
from urllib.request import urlopen

data = pickle.load(urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
# print(data)

for line in data:
    print("".join([k * v for k, v in line]))