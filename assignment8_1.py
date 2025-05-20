import threading

def even(no) :
    for i in range(1, no) :
        if i % 2 == 0 :
            print("even numbers are :",i)

def odd(no) :
    for i in range(1, no) :
        if i % 2 != 0 :
            print("odd numbers are :",i)

def main() :

    t1 = threading.Thread(target = even, args = (10,))
    t2 = threading.Thread(target = odd, args = (10,))

    t1.start()
    t2.start()

if __name__ == "__main__" :
    main()


