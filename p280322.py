# Работа со строками

str = "Пример строки"
str2 = "Example string"

outstr = str.encode()
print(outstr)


outstr2 = str2.encode('ascii',errors='ignore')
print(outstr2)
