from string import ascii_letters
class Semelein:
    _S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    _S_RUS_UPPER = _S_RUS.upper()

    def __init__(self,fio,old,ps,weight):
        self.verification_fio(fio)

        self.__fio = fio.split() # список
        self.__old = old # целое число
        self.__pass = ps # строка
        self.__weight = weight

    @classmethod
    def verification_fio(cls,fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')

        f= fio.split()
        if len(f)!=3:
            raise TypeError('Не верный формат ФИО')

        letters = ascii_letters + cls._S_RUS + cls._S_RUS_UPPER
        for s in f:
            if len(s)<1:
                raise TypeError('В ФИО должен быть хотя бы один символ')
            if len(s.strip(letters))!=0:
                raise TypeError('В ФИО нужно использовать только буквы')

    @classmethod
    def verification_old(cls,old):
        if type(old) != int or old <14 or old >120:
            raise TypeError('Возраст должен быть целым числом в диапозоне от 14 до 120')

obj = Semelein('Вушняков Сергей Валерьевич',51,'123',83.200)
print(obj.__dict__)

