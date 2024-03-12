import time
import datetime
ct = str(datetime.datetime.now())
#ct = ct.split()
#dt, tm = ct[0].split('-'), ct[1].split(':')

time_difference = 8*60*60
ctsec = time.time()


def reed():
    global ctsec, time_difference, line
    try:
        txt = open('datp.txt', 'r')
        line = float(txt.readlines()[0])
        txt.close()
    except:
        print('Running for the first time. Hmm.......')
        line = ctsec - time_difference - 1


def write():
    global ctsec
    txt = open('datp.txt', 'w')
    txt.write(str(ctsec))


def log():
    global ct
    txt = open('logdt.txt', 'a')

    txt.write(ct + '\n')
    txt.close()


def main():
    reed()
    global line, time_difference, ctsec
    if ctsec - line > time_difference:
        write()
        log()
        print ('u can eat')
    else:
        print('Its less than 8 hours, pls wait.')


main()
time.sleep(60)



