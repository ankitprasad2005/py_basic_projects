import pyperclip
import time
import os

def apt():
    global temp
    txt = open("clipboard.txt","a")
    temp = pyperclip.paste()
    txt.write("\n" + temp)
    txt.close()

apt()
n,n1 = 0,100
while n in range(n1):
    n1 += 1

    if pyperclip.paste() == temp:
        time.sleep(1)
        
    else:
        temp = pyperclip.paste()
        apt()