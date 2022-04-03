# Работа с фйлами xlsx

import openpyxl
wb = openpyxl.load_workbook('myfile.xlsx')
sheet = wb['main']
val = sheet['A1'].value
print(val)
val2 = sheet['B1'].value
print(val2)
print(type(val))
print(type(val2))
wb.close()


