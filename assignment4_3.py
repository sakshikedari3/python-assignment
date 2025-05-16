import sys
from functools import reduce

def main():
    data = []
    if len(sys.argv) > 1 :
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("Enter the size of elements you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the element : "))
            data.append(a)

    fData = list(filter(lambda no : no >= 70 and no <= 90, data))
    print(fData)

    mData = list(map(lambda no: no + 10, fData))
    print(mData)

    rData = reduce(lambda no1, no2 : no1 + no2, mData)
    print(rData)

    print("result is : ",rData)

if __name__ == "__main__" :
    main()