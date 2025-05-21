from multiprocessing import Pool

def factorial(n):
    a = 1
    for i in range(n, 1, -1) :
        a = a * i
    return a

def main() :
    data = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    result = []

    p = Pool()
    result = p.map(factorial, data)

    p.close()
    p.join()

    print(result)

if __name__ == "__main__" :
    main()
