from string import ascii_letters
class Semelein:
    _S_RUS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    _S_RUS_UPPER = _S_RUS.upper()

    def __init__(self,fio,old,ps,weight):
        self.verification_fio(fio)
        self.verification_old(old)
        self.verification_weight(weight)
        self.verification_ps(ps)

        self.__fio = fio.split() # список
        self.__old = old # целое число
        self.__ps = ps # строка
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

    @classmethod
    def verification_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError('Вес должен быть вещественным числом от 20')

    @classmethod
    def verification_ps(cls,ps):
        if type(ps)!=str:
            raise TypeError('Паспорт должен быть строкой')
        s= ps.split()
        if len(s)!=2 or len(s[0])!=4 or len(s[1])!=6:
            raise TypeError('Неверный формат данных паспорта')
        for p in s:
            if not p.isdigit():
                raise TypeError('Номер паспорта должна быть числами')

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self,old):
        self.verification_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verification_weight(weight)
        self.__weight = weight

    @property
    def pasport(self):
        return self.__ps

    @pasport.setter
    def pasport(self, ps):
        self.verification_ps(ps)
        self.__ps = ps


obj = Semelein('Вушняков Сергей Валерьевич',51,'1234 123456',83.200)
print(obj.__dict__)