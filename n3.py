class StripChars:
    def __init__(self,chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0],str):
            raise TypeError("Аргумент должен быть строкой")

        return args[0].strip(self.__chars)

s1 = StripChars("?:!.; ")

res= s1(" Hello World!! ")
print(res)