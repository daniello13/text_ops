# -*- coding: utf-8 -*-
from math import *
from math import *

def average(text):jkhbkjhkj
    mas = text.split()
    Xsr = i = 0
    while i < len(mas):
        Xsr += len(mas[i]) #находим среднее арифметическое длин слов
        i+=1	
    Xsr/=len(mas)
    return Xsr

def dispersion(text):
    mas = text.split()
    dis = i = 0
    Xsr = average(text)
    while i <len(mas):
        dis += (len(mas[i])-Xsr)*(len(mas[i])-Xsr)
        i+=1
    dis/= len(mas)
    dis = sqrt(dis)
    return dis
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
def split_text(filename):
	fdes = open(filename, 'r', encoding='utf-8') # opening file
	text = fdes.read() # reading
	fdes.close()
	return text.split()

#print("Введите имя файла: ")
#filename=input() # choosing file
try:
	texts = []
	#a.append([]) # создаем пустую строку
	texts.append(split_text('A_Fashion.txt'))
	texts.append(split_text('B_Politics.txt'))
	texts.append(split_text('C_Science.txt'))
	texts.append(split_text('D_Sport.txt'))
	texts.append(split_text('E_Incident.txt'))
		#for c in range(10): # в каждой строке - 10 элементов
		#	a[r].append(k) # добавляем очередной элемент в строку
		#	k += 1 # увеличиваем значение счетчик
except FileNotFoundError:
	print("Файл не найден")
	exit()
#print(text) # prints all text to console
print("s.k.o.: ")
print(deviation(text))
print("dispersion:")
print(dispersion(text))
