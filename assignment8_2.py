import threading

def even(no) :
    a = 0
    for i in range(1, no) :
        if i % 2 == 0 :
            a = a + i
            print("Even number :",i)
    print("sum of even numbers are :",a)

def odd(no) :
    a = 0
    for i in range(1, no) :
        if i % 2 != 0 :
            a = a + i
            print("odd number :",i)
    print("sum of odd numbers are :",a)

def main() :
    no = int(input("Enter the number : "))

    t1 = threading.Thread(target = even, args = (no,))
    t2 = threading.Thread(target = odd, args = (no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from main")

if __name__ == "__main__" :
    main()


