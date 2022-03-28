import allfunc

allfunc.myfunc()

automobil = ["v1","m2","j3","z4"]
for one_auto_index,one_auto_var in enumerate(automobil):
	print(one_auto_index,"==",one_auto_var)

print(id(automobil))
print(type(automobil))

resx = ('asd','qwe','wer')
print(id(resx))
print(type(resx))

d = {(1, 1, 1) : 1}
print(d.__sizeof__())

ex2 =  list('список')
print(ex2)
print(dir())