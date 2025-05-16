# area and perameter
import sys

def area(value1, value2) :
    area = value1 * value2
    print("Area is :",area)

    perimeter = 2 * (value1 + value2) 
    print("Perimeter is :",perimeter)

def main() :
    if len(sys.argv) == 3 :
        length = int(sys.argv[1])
        width = int(sys.argv[2])

    else :
        length = int(input("Enter the length of rectangle : "))
        width = int(input("Enter the width of rectangle : "))

    area(length, width)

if __name__ == "__main__" :
    main()
