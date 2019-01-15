# -*- coding: utf-8 -*-
from functions import *

try:
	texts = []
	texts.append(split_text('A_Fashion.txt'))
	texts.append(split_text('B_Politics.txt'))
	texts.append(split_text('C_Science.txt'))
	texts.append(split_text('D_Sport.txt'))
	texts.append(split_text('E_Incident.txt'))
	NUM_OF_WORDS = len(texts[0])+len(texts[1])+len(texts[2])+len(texts[3])+len(texts[4])
except FileNotFoundError:
	print("Файл не найден")
	exit()
namefiles = ["A_Fashion","B_Politics", "C_Science", "D_Sport","E_Incident"]
while True:
	case = input('Выберите вариант: \n1. подсчет слов \n2. сравнение частот \n3. среднее арифметическое \n4. медиана\n5. мода\n6. мера среднеквадратического отклонения \n7. коэффициент вариации \nВаш выбор: ')
	if case == '7':
		slovo=input('Введите слово для определения коэффициента вариации в корпусе: ')
		print("Коэффициент вариации: %.2f %%" % (juilland(slovo,namefiles)*100))
	if case == '6':
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
	elif case == '1':
		print("------------------------------------------------Подсчет слов------------------------------------------------")
		choise1=input('Введите слово для определения частотности в корпусе: ')
		kol = podschet_slov(choise1)
		print("\nСлово повторяется в корпусе %i раз(а), что составляет частотность вхождений %.3f%% " % (int(kol), (100*float(kol))/NUM_OF_WORDS))
	elif case == '2':
		print("------------------------------------------------ Абсолютная частота и относительная ------------------------------------------------")
		choise1=input('Введите слово для определения частотности в корпусе: ')
		kol = podschet_slov(choise1)
		print("\nСлово повторяется во всем корпусе %i раз(а), что составляет абсолютную частоту вхождений %.3f%% " % (int(kol), (100*float(kol))/NUM_OF_WORDS))
		print("------------------------------------------------ Oтносительная частота ------------------------------------------------")
		for i in namefiles:
			print("\nСлово повторяется в подкорпусе %s %i раз(а), что составляет относительную частоту %.3f%%" % (i, otnosit_chast(i, choise1), otnosit_chast(i, choise1)*100/kol_vo_slov(i+'.txt')))