# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 12:16:46 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/linkedlist.php
'''

import requests
import bs4

room4 = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022')
# print(room4.text)
napis = str(room4.text)
tabelka = napis.split(' ')
nastepny = tabelka[-1]
liczba_skokow = 85

while True:
    
    petla = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nastepny}')
    nowy_napis = str(petla.text)
    print('\n' + nowy_napis)
    tabelka = nowy_napis.split(' ')
    nastepny = tabelka[-1]
    print(nastepny)
    try:
        nastepny = int(nastepny)
        liczba_skokow +=1
        print(f'Jestem na {liczba_skokow} stronie')
    except:
        break