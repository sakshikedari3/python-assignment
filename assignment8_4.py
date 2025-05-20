import threading
import os

def small(value) :
    print("pid of thread is :",os.getpid())
    tname = threading.current_thread().name
    print(tname)
    a = 0
    b = []
    for i in value :
        if i.islower() :
            a = a + 1
            b.append(i)
    print("b :",b)
    print("small : ",a)

def captial(value) :
    print("pid of thread is :",os.getpid())
    tname = threading.current_thread().name
    print(tname)
    a = 0
    b = []
    for i in value :
        if i.isupper() :
            a = a + 1
            b.append(i)
    print("b :",b)
    print("captial :",a)

def digit(value) :
    print("pid of thread is :",os.getpid())
    tname = threading.current_thread().name
    print(tname)
    a = 0
    b = []
    for i in value :
        if i.isdigit() :
            a = a + 1
            b.append(i)
    print("b :",b)
    print("digit :",a)

def main () :
    name = input("Enter the string : ")

    t1 = threading.Thread(target = small, args = (name,))
    t2 = threading.Thread(target = captial, args = (name,))
    t3 = threading.Thread(target = digit, args = (name,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__" :
    main()