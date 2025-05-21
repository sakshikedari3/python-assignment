from functools import reduce

def main():
    data = []
    size = int(input("Enter the size of elements you want to enter : "))

    for n in range(size) :
        a = int(input("Enter the element : "))
        data.append(a)

    fData = list(filter(lambda no : no % 2 == 0, data))
    print(fData)

    mData = list(map(lambda no: no * no, fData))
    print(mData)

    rData = reduce(lambda no1, no2 : no1 + no2, mData)
    print(rData)

    print("result is : ",rData)

if __name__ == "__main__" :
    main()