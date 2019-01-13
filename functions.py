# -*- coding: utf-8 -*-
from math import *
import re
from collections import Counter

def average(mas):
    Xsr = i = 0
    while i < len(mas):
        Xsr += len(mas[i]) #находим среднее арифметическое длин слов
        i+=1	
    Xsr/=len(mas)
    return Xsr

def dispersion(mas):
    dis = i = 0
    Xsr = average(mas)
    while i <len(mas):
        dis += (len(mas[i])-Xsr)*(len(mas[i])-Xsr)
        i+=1
    dis/= len(mas)
    return dis

def deviation(mas):
	return sqrt(dispersion(mas))

def split_text(filename):
	fdes = open(filename, 'r', encoding='utf-8') # opening file
	text = fdes.read() # reading
	fdes.close()
	return text.split()

def sortByLength(inputStr):
        return len(inputStr)

def mediana(mas):
    tmp=mas
    tmp.sort(key=len)
    ser = int(len(tmp)/2)
    return len(tmp[ser])

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def moda(mas):
    a=[]
    for i in mas:
        a.append(len(i))
    tmp = frozenset(a)
    d={}
    for k in tmp:
        c=0
        for i in mas:
            if len(i)==k:
                c+=1
        d[k]=c
    max_used=0
    kol_voBukw=0
    max_used = max(d.values())
    kol_voBukw = get_key(d, max_used)
    return kol_voBukw

def reading_fileToOneString(filename):
    f = open(filename, 'r', encoding='utf-8')
    string = f.read()
    f.close()
    return string

def podschet_slov(find_it):
    texts = ''
    texts+=reading_fileToOneString('A_Fashion.txt')
    texts+=reading_fileToOneString('B_Politics.txt')
    texts+=reading_fileToOneString('C_Science.txt')
    texts+=reading_fileToOneString('D_Sport.txt')
    texts+=reading_fileToOneString('E_Incident.txt')

    words = re.findall(find_it, texts)
    return len(words)

