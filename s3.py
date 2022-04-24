class Example:
    param = 1000

    def cheng_param(self,inner_param):
        self.param = inner_param

    @classmethod
    def gl_cheng_param(cls,gl_inner_param):
        cls.param = gl_inner_param

pn1 = Example()
pn1.cheng_param(200)
pn1.gl_cheng_param(300)
print(pn1.__dict__)
print(Example.__dict__)
