
def fac(x):
    if x == 1 or x == 0:
        return 1
    return x * fac(x-1)

print(fac(int(input())))

