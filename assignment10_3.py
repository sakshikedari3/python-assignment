from functools import reduce

def main() :
    data = []
    size = int(input("Enter the number of element you want to enter : "))

    for n in range(size) :
        a = int(input("Enter the element : "))
        data.append(a)

    print("Data is :",data)

    fdata = list(filter(lambda x : x >= 70 and x <= 90, data))
    print("Filter data is :",fdata)

    mdata = list(map(lambda x : x + 10, fdata))
    print("maped data is :",mdata)

    rdata = reduce(lambda x, y : x + y, mdata)
    print("reduced data is :",rdata)

if __name__ == "__main__" :
    main()