#map double list
import sys

def main():
    data = []
    if len(sys.argv) > 2 :
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("enter the number of element you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the element : "))
            data.append(a)

    print(data)

    mData = list(map(lambda no : no + no , data))

    print("result is :",mData)

if __name__ == "__main__" :
    main()