from threading import Thread
from multiprocessing import Process
import time

def numbers(value) :
    a = 0
    for i in range(1, value) :
        a += i
    return a

def main ():

    start1 = time.time()

    result = numbers(10000000)

    print("Result is :", result)

    end1 = time.time()

    print("Time taken by normal function is :", end1 - start1)

    start2 = time.time()
    t1 = Thread(target = numbers, args = (10000000,))

    t1.start()
    t1.join()
    
    end2 = time.time()
    print("Time taken by Thread:", end2 - start2)

    start3 = time.time()

    p1 = Process(target = numbers, args = (10000000,))

    p1.start()
    p1.join()

    end3 = time.time()
    print("Time taken by Process:", end3 - start3)

if __name__ == "__main__":
    main()

