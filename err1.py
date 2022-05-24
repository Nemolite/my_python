try:
    f = open("test23.txt")
except FileNotFoundError:
    print("Невозможно открыть файл")

try:
    x, y = map(int, input().split())
    res = x/y
except (ValueError,ZeroDivisionError):
    print("Ошибка типа данных")
#except ZeroDivisionError:
#    print("Деление на ноль")

print("Штатное завершение")