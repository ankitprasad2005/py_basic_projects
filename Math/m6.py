
class mt(object):
    def __init__(self, x):
        self.x = x
       
    def fac(self):
        if self.x == mt(1) or self.x == mt(0):
            return 1
        return print(self.x * mt.fac(x-1))

a = mt(10)
print(type(a))
mt.fac(10)
