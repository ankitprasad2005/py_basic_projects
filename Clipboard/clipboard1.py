import pyperclip
import time

def ad():
    global temp
    txt = open("clipboard.txt","a")
    temp = pyperclip.paste()
    txt.write(temp + "\n")
    txt.close()
    wt()

def wt():
    global temp
    if pyperclip.paste() == temp:
        time.sleep(1)
        wt()
    else:
        ad()

ad()