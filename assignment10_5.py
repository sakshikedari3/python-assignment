from functools import reduce

def prime(value) :
    if value < 2 :
        return False
    for i in range(2, value):
        if value % i == 0 :
            return False     
        else :
            return True
            
def maximum_num(a, b) :
    if b > a :
        a = b

    return a

def main() :
    data = []
    size = int(input("Enter the number of element you want to enter : "))

    for _ in range(size) :
        a = int(input("Enter the element : "))
        data.append(a)

    fdata = list(filter(prime, data))
    print("Filter data is :",fdata)

    mdata = list(map(lambda x : x * 2, fdata))
    print("maped data is :",mdata)

    rdata = reduce(maximum_num, mdata)
    print("Reduce data is :",rdata)

if __name__ == "__main__" :
    main()

