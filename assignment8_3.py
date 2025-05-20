import threading

def even(value) :
    j = []
    a = 0
    for i in value :
        if i % 2 == 0 :
            a = a + i
            j.append(i)
    print("list :",j)
    print("sum of even numbers in list is :",a)

def odd(value) :
    j = []
    a = 0
    for i in value :
        if i % 2 != 0 :
            a = a + i
            j.append(i)
    print("list :",j)
    print("sum of odd numbers in list is :",a)

def main() :
    data = []
    size = int(input("Enter the number of elements you want to enter : "))

    for n in range(size) :
        b = int(input("Enter the element : "))
        data.append(b)

    print("data :",data)

    t1 = threading.Thread(target = even, args = (data,))
    t2 = threading.Thread(target = odd, args = (data,))

    t1.start()
    t2.start()

if __name__ == "__main__" :
    main()


