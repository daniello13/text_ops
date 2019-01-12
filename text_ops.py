# -*- coding: utf-8 -*-
from math import *

def deviation(text):
	mas = text.split() #разбиваем текст на слова
	Xsr = i=0 
	while i < len(mas):
		Xsr += len(mas[i]) #находим среднее арифметическое длин слов
		i+=1	
	Xsr/=len(mas)
	stdev = i = 0
	while i<len(mas):
		stdev += fabs(len(mas[i]) - Xsr) #находим стандартное отклонение
		i+=1
	stdev/=len(mas)
	return stdev


print("Введите имя файла: ")
filename=input() # choosing file
try:
	fdes = open(filename, 'r', encoding='utf-8') # opening file
	text = fdes.read() # reading
	fdes.close() #closing
except FileNotFoundError:
	print("Файл не найден")
	exit()
#print(text) # prints all text to console
print(deviation(text))
#D:\Downloads\texts\A_Fashion.txt
