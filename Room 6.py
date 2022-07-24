# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:01:50 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/channel.html
'''

import zipfile

#unzipping
# zip_obj = zipfile.ZipFile('channel.zip','r')
# zip_obj.extractall('channel')
# zip_obj.close()

instrukcja = open('channel\\readme.txt','r')
print(instrukcja.read())
instrukcja.close()

plik = open('channel\\90052.txt','r')
zawartosc = plik.read()
plik.close()
print(zawartosc)
zawartosc_podzielona = zawartosc.split(' ')
nastepny = zawartosc_podzielona[-1]
liczba_skokow = 1

while True:
    
    plik = open(f'channel\\{nastepny}.txt','r')
    zawartosc = plik.read()
    plik.close()
    print(zawartosc)
    zawartosc_podzielona = zawartosc.split(' ')
    nastepny = zawartosc_podzielona[-1]
    
    try:
        nastepny = int(nastepny)
        liczba_skokow +=1
        print(f'Jestem na {liczba_skokow} stronie')
    except:
        break