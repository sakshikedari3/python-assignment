#filter prime no
import sys

def prime(n):
    if n < 2:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True 

def main():
    data = []
    if len(sys.argv) > 2 :
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("Enter the number you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the number : "))
            data.append(a)

    print(data)

    fdata = list(filter(prime, data))
    print("filter data is :",fdata)

if __name__ == "__main__" :
    main()