def checkinput():
    try:
        return int(input())
    except:
        print('please enter an integer')
        return checkinput()


'''
def checkinput():
    try:
        return int(input())
    except:
        print('please enter an integer')
        checkinput()
'''


num = 10
a = checkinput()

while a != num:
    if a > num:
        print('something smaller')
        a = checkinput()
    if a < num:
        print('somemthing larger')
        a = checkinput()

print('you win')
