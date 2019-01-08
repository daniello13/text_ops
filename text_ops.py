# -*- coding: utf-8 -*-
#changes Viktoriya
print("Введите имя файла: ")
filename=input() # choosing file
try:
	fdes = open(filename) # opening file 
	text = fdes.read() # reading
	fdes.close() #closing
except FileNotFoundError:
	print("Файл не найден")
	exit()
print(text) # prints all text to console
