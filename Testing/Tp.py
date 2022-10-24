txt = open('Write speed.txt', 'w')
n = int(input())
x = 0
while x <= n:
    txt.write('0')
    x = x + 1
txt.close()
