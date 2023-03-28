def fn1(a, b, c):
    d = 0
    for x in range(c):
        d = d + a
        a = a * b
    return print(d)

fn1(4, 2, 3)


class cl():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def gp(self):
        d = 0
        for x in range(self.c):
            d = d + self.a
            self.a = self.a * self.b
        return print(d)

a = cl(4,2,3)
a.gp()


import time
t1 = time.time()
fn1(1, 10, 10)
t2 = time.time()
a.gp()
t3 = time.time()
print(t2-t1)
print(t3-t2)




