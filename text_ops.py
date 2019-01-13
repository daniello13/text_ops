# -*- coding: utf-8 -*-
from functions import *

try:
	texts = []
	texts.append(split_text('A_Fashion.txt'))
	texts.append(split_text('B_Politics.txt'))
	texts.append(split_text('C_Science.txt'))
	texts.append(split_text('D_Sport.txt'))
	texts.append(split_text('E_Incident.txt'))
except FileNotFoundError:
	print("Файл не найден")
	exit()
namefiles = ["A_Fashion","B_Politics", "C_Science", "D_Sport","E_Incident"]
case = input('Выберите вариант: \n1. подсчет слов \n2. сравнение частот \n3. среднее арифметическое \n4. медиана\n5. мода\n6. описание распредeлений \n7. мера среднеквадратического отклонения \n8. коэффициент вариации \nВаш выбор: ')
if case == '8':
	print("------------------------------------------------Среднеквадратичное отклонение------------------------------------------------")
	i=0
	while i < 5:
		print(namefiles[i] + ": ")
		print(deviation(texts[i]))
		i+=1
if case == '7':
	print("------------------------------------------------Мера среднеквадратичного отклонения------------------------------------------------")
	i=0
	while i < 5:
		print(namefiles[i] + ": ")
		print(dispersion(texts[i]))
		i+=1
elif case == '3':
	print("------------------------------------------------Среднее арифметическое------------------------------------------------")
	choise1=input('Выберите текст: \n0 A_Fashion.txt \n1 B_Politics.txt \n2 C_Science.txt \n3 D_Sport.txt \n4 E_Incident.txt \nВаш выбор: ')
	print("\nСреднее арифметическое: %.3f" % average(texts[int(choise1)]))
elif case == '4':
	print("------------------------------------------------Медиана------------------------------------------------")
	choise1=input('Выберите текст: \n0 A_Fashion.txt \n1 B_Politics.txt \n2 C_Science.txt \n3 D_Sport.txt \n4 E_Incident.txt \nВаш выбор: ')
	print("\nМедиана: %i" % mediana(texts[int(choise1)]))
elif case == '5':
	print("------------------------------------------------Мода------------------------------------------------")
	choise1=input('Выберите текст: \n0 A_Fashion.txt \n1 B_Politics.txt \n2 C_Science.txt \n3 D_Sport.txt \n4 E_Incident.txt \nВаш выбор: ')
	print("\nМода: %i" % moda(texts[int(choise1)]))