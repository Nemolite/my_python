class ExceptionPrintSendData(Exception):
    """ Класс исключения при отправке данных принтеру"""
    def __init__(self,*args):
        self.messege = args[0] if args else None

    def __str__(self):
        return f"Ошибка {self.messege}"

class PrintData:
    def print(self,data):
        self.send_data(data)
        print(f"печать{str(data)}")

    def send_data(self,data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData("принтер не отвечает")

    def send_to_print(self,data):
        return False


p = PrintData()
p.print("123")
# try:
#     p.print("123")
# except Exception:
#     print("принтер не отвечает")