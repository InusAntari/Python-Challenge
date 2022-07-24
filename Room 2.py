# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 22:30:52 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/ocr.html
'''

'''import tekstu z pliku'''
f2r = open('C:\\Users\\Tomek\\OneDrive\\Szkolenie Python\\Python Challenge\\Room2.txt', mode = 'r')
kod = f2r.read()
f2r.close

'''separacja znakow'''
kod_split = []
for znak in kod:
    kod_split.append(znak)

'''znalezienie unikatowych znakow'''
kod_unique = []
for znak in kod_split:
    if znak not in kod_unique:
        kod_unique.append(znak)
    else:
        pass
unikatowe_znaki ={}
for znak in kod_unique:
    unikatowe_znaki[znak] = 0
    
'''przypisanie, ile razy dany znak wystepuje'''
for znak in kod_split:
     unikatowe_znaki[znak] +=1
wynik=''

'''wyszukanie tylko tych znakow, ktore wystepuja raz i utworzenie z nich stringa'''
for znak in unikatowe_znaki:
    if unikatowe_znaki[znak]==1:
        wynik += znak
    else:
        pass
print(wynik)