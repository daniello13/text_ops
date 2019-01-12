# -*- coding: utf-8 -*-
from math import *

def coefDis(texts):
    coef=0
    i=0
    while i < 5:
        coef += dispersion(texts[i])
        i+=1

def average(mas):
    Xsr = i = 0
    while i < len(mas):
        Xsr += len(mas[i]) #находим среднее арифметическое длин слов
        i+=1	
    Xsr/=len(mas)
    return Xsr

def dispersion(mas):
    return deviation(mas)^2

def deviation(mas):
	Xsr = average(mas)
	stdev = i = 0
	while i<len(mas):
		stdev += (len(mas[i])-Xsr)*(len(mas[i])-Xsr) #находим ско
		i+=1
	stdev/=len(mas)
	stdev = sqrt(stdev)
	return stdev

def split_text(filename):
	fdes = open(filename, 'r', encoding='utf-8') # opening file
	text = fdes.read() # reading
	fdes.close()
	return text.split()