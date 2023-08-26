b = input().split()
a = []
for i in b:
    a.append(int(i))
a.sort()
p = len(a) - 1
for x in range (p+1):
    if a[p-x] != a[p-(x+1)]:
        print (a[p-(x+1)])
        break
