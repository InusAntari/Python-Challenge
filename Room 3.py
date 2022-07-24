# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:14:34 2022

@author: Tomek
"""

'''
http://www.pythonchallenge.com/pc/def/equality.html
'''
import re

'''import tekstu z pliku'''
f2r = open('C:\\Users\\Tomek\\OneDrive\\Szkolenie Python\\Python Challenge\\Room3.txt', mode = 'r')
kod = f2r.read()
f2r.close

print (''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',open("C:\\Users\\Tomek\\OneDrive\\Szkolenie Python\\Python Challenge\\Room3.txt").read())))


# alfabet_z_malej = 'abcdefghijklmnopqrstuvwxyz'
# alfabet_z_wielkiej = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# alfabet_z_malej2 = []
# alfabet_z_wielkiej2 = []
# for litera in alfabet_z_malej:
#     alfabet_z_malej2.append(litera)
# for litera in alfabet_z_wielkiej:
#     alfabet_z_wielkiej2.append(litera)

# '''separacja znakow'''
# kod_split = []
# for znak in kod:
#     kod_split.append(znak)

# '''znalezienie tej jednej malej litery'''
# male_litery = []
# for index, litera in enumerate(kod_split):
#     if index < 3 or index > 101247:
#         pass
#     elif litera in alfabet_z_malej2:
#         if kod_split[index-3] in alfabet_z_wielkiej2 and  kod_split[index-2] in alfabet_z_wielkiej2 and kod_split[index-1] in alfabet_z_wielkiej2 and kod_split[index+1] in alfabet_z_wielkiej2 and kod_split[index+2] in alfabet_z_wielkiej2 and kod_split[index+3] in alfabet_z_wielkiej2:
#             male_litery.append(str(litera))
#             # print(kod_split[index-3]+kod_split[index-2]+kod_split[index-1]+litera+kod_split[index+1]+kod_split[index+2]+kod_split[index+3])
#     else:
#         pass

# kod_unique = []
# for znak in male_litery:
#     if znak not in kod_unique:
#         kod_unique.append(znak)
#     else:
#         pass

# wynik = ''
# for litera in kod_unique:
#     wynik += litera