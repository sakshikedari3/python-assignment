import time
from threading import Thread

def number(value) :
    for i in range(1, value + 1) :
        print(i)

def main () :

    t1 = Thread(target = number, args = (5,))
    t2 = Thread(target = number, args = (5,))
    time.sleep(1)
    t3 = Thread(target = number, args = (5,))
    time.sleep(1)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__" :
    main()

    