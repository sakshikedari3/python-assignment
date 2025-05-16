import sys
from functools import reduce

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def max_num(a, b) :
    if b > a :
        a = b
    return a

def main():
    data = []
    if len(sys.argv) > 2 :
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("Enter the number of element you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the number of elememt : "))
            data.append(a)

    fData = list(filter(prime, data))
    print(fData)

    mData = list(map(lambda no : no * 2, fData))
    print(mData)

    rData = reduce(max_num, mData)
    print(rData)

if __name__ == "__main__" :
    main()