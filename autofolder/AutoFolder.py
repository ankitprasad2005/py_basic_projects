import datetime
import time
import os
import pyperclip

cp = os.getcwd()
os.chdir(cp)

def crt():
    global ld, cd, cp, pp, pc, pm
    try:
        os.chdir(pp)
        os.makedirs(cd)
        os.chdir(pc)
        os.makedirs(cd)
        os.chdir(pm)
        os.makedirs(cd)
        os.chdir(cp)
        ld = cd
    except:
        print('\nThe folder (which you want to create) already exist.')
        time.sleep(30)
        exit()


def crtc():
    global pp, pc, pm, cd, cp, ld
    print('\nWhich subject folder to create?    {p,c,m}')
    inp4 = input()
    print()
    try:
        if inp4 == 'p' or inp4 == 'P':
            os.chdir(pp)
            os.makedirs(cd)
        elif inp4 == 'c' or inp4 == 'C':
            os.chdir(pc)
            os.makedirs(cd)
        elif inp4 == 'm' or inp4 == 'M':
            os.chdir(pm)
            os.makedirs(cd)
        os.chdir(cp)
        ld = cd
    except:
        print("\nRelaunch and enter correct credentials.")
        time.sleep(30)
        exit()


def dtct():
    global cd, ld
    inp2 = input('Enter Folder name: ')
    cd = inp2


def ptcp():
    global pp, pc, pm
    print('\nWhich path to change?  (p,c,m,a(all))')
    inp3 = input()
    if inp3 == 'p' or inp3 == 'P':
        pp = input('Enter new Physics path:').strip()
    elif inp3 == 'c' or inp3 == 'C':
        pc = input('Enter new Chemistry path:').strip()
    elif inp3 == 'm' or inp3 == 'M':
        pm = input('Enter new Maths path:').strip()
    elif inp3 == 'a' or inp3 == 'A':
        pp = input('Enter new Physics path:').strip()
        pc = input('Enter new Chemistary path:').strip()
        pm = input('Enter new Maths path:').strip()
    else:
        print("\nRelaunch and enter correct credentials.")
        time.sleep(30)
        exit()


def svpt():
    global ld, cd, pp, pc, pm
    txt2 = open('datp.txt', 'w')
    txt2.write(ld+'\n'+pp+'\n'+pc+'\n'+pm)
    txt2.close()


def verf():
    try:
        os.chdir(pp)
        os.chdir(pc)
        os.chdir(pm)
        os.chdir(cp)
    except:
        print('\nPlease relaunch the application and enter the folder path again (In menu 3),  OR  The folder already exist.')
        time.sleep(30)
        exit()


def svptd():
    global ld, cd, pp, pc, pm
    txt3 = open('datp.txt', 'w')
    txt3.write(cd+'\n'+pp+'\n'+pc+'\n'+pm)
    txt3.close()




ct = str(datetime.datetime.now())
tm = ct.split('-')
d0 = tm[2]
d1 = d0.split()

dt = d1[0]
mn = tm[1]
yr = tm[0]
cd = dt + "." + mn + "." + yr

try:
    txt1 = open('datp.txt', 'r')
    list1 = txt1.readlines()
    list2 = []
    for ln in list1:
        if ln[-1] == '\n':
            list2.append(ln.strip('\n'))
        else:
            list2.append(ln)
    txt1.close()
    
    ld = list2[0]
    pp = list2[1]
    pc = list2[2]
    pm = list2[3]
    print('\nDefault date and paths:-', '\n', cd, '\n', ld, '\n', pp, '\n', pc, '\n', pm, '\n')
    
except:
    print('\nOpening the app for first time. \nPls enter the required path: \n')
    ld = cd
    pp = input('Enter new Physics path:').strip()
    pc = input('Enter new Chemistary path:').strip()
    pm = input('Enter new Maths path:').strip()
    try:
        verf()
    except:
        print('\nPlease relaunch the application and enter the folder path again (In menu 3),  OR  The folder already exist.')
        time.sleep(30)
        exit()
    svptd()
    print('\n\n')




print('\n1 ==> Run as default \n2 ==> Run partially \n3 ==> Edit Data(temporary) & Create \n4 ==> Edit Path(Permanent) & Create \n5 ==> Edit Both & Create \n6 ==> Edit Path only \n7 ==> Copy path to Clipboard')
try:
    inp1 = int(input())
    print()
    if inp1 == 1:
        crt()
        svptd()
    
    elif inp1 == 2:
        crtc()
        svptd()

    elif inp1 == 3:
        dtct()
        crt()
        svptd()

    elif inp1 == 4:
        ptcp()
        verf()
        crt()
        svptd()
    
    elif inp1 == 5:
        dtct()
        ptcp()
        verf()
        crt()
        svptd()
        
    elif inp1 == 6:
        ptcp()
        verf()
        svpt()
        
    elif inp1 == 00 or inp1 == 7:
        print()
except:
    print("\nRelaunch and enter correct credentials")
    time.sleep(30)
    exit()




bs = "\\"
pp1 = pp+bs+ld
pc1 = pc+bs+ld
pm1 = pm+bs+ld


print('\n\nWant to copy folder destination to clipboard? \n{p,c,m,a(all),  d(date),     n => no}')
inp6 = input()
print()
if inp6 == 'p' or inp6 == 'P':
    pyperclip.copy(pp1)
    
elif inp6 == 'c' or inp6 == 'C':
    pyperclip.copy(pc1)
    
elif inp6 == 'm' or inp6 == 'M':
    pyperclip.copy(pm1)
    
elif inp6 == 'a' or inp6 == 'A':
    try:
        num6 = int(input('Enter Delay (sec): '))
    except:
        print("\nRelaunch and enter correct credentials")
        time.sleep(90)
        exit()
    pyperclip.copy(pp1)
    time.sleep(num6)
    pyperclip.copy(pc1)
    time.sleep(num6)
    pyperclip.copy(pm1)
    time.sleep(num6)
    pyperclip.copy(ld)
    time.sleep(num6)

elif inp6 == 'd' or inp6 == 'D':
    pyperclip.copy(ld)
    
elif inp6 == 'n' or inp6 == 'N':
    print()
    
else:
    print("\nRelaunch and enter correct credentials")
    time.sleep(90)
    exit()



print('\n ')
if inp1 == 3:
    print('successfully edited date.')
if inp1 == 4 or inp1 == 5 or inp1 == 6:
    print('successfully edited file path.')
if inp1 == 1 or inp1 == 2 or inp1 == 3 or inp1 == 4 or inp1 == 5:
    print('Successfully created 3 folders.')
if inp1 == 7:
    print('Successfully Copied file path to clipboard.')
time.sleep(30)

