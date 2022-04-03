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


 

