#filter even no
import sys

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

    fdata = list(filter(lambda no : (no % 2 == 0), data))
    print("filter data is :",fdata)

if __name__ == "__main__" :
    main()