from multiprocessing import Process

def square(value):
    a = 1
    for i in value :
        a =i * i
        print(a)

def main () :
    data1 = [2,5,8,9,10,30,60,82,100]
    data2 = [1,2,3,4,5,6,7,8,9]
    data3 = [10,20,30,40,50,60,70,80,90]

    print("Process 1")

    p1 = Process(target = square, args = (data1,))

    p2 = Process(target = square, args = (data2,))

    p3 = Process(target = square, args = (data3,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == "__main__" :
    main()