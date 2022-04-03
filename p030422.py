# Работа  файлами

obfile = open("names.txt")
for linefil in obfile.readlines():
	print(linefil)
	print(type(linefil))
	a = linefil.split(' ')
	print(a)
for fin in a:
	if fin == 'test':
		print('да')
	else:
		print('нет')


 

# Работа с фйлами xlsx

import openpyxl
wb = openpyxl.load_workbook('myfile.xlsx')
sheet = wb['main']
val = sheet['A1'].value
print(val)
val = sheet['B1'].value
print(val)
print(type(val))
wb.close()


