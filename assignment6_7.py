#maximum of 3 number
import sys

def maximum(value1, value2, value3, value4, value5) :
    a = 0
    if value1 > a :
        a = value1

    if value2 > a :
        a = value2

    if value3 > a :
        a = value3

    if value4 > a :
        a = value4

    if value5 > a :
        a = value5
    
    print("maximum number is : ",a)

def main():
    if len(sys.argv) == 6 :
        no1 = int(sys.argv[1])
        no2 = int(sys.argv[2])
        no3 = int(sys.argv[3])
        no4 = int(sys.argv[4])
        no5 = int(sys.argv[5])

    else :
        no1 = int(input("Enter the first number : "))
        no2 = int(input("Enter the second number : "))
        no3 = int(input("Enter the third number : "))
        no4 = int(input("Enter the fouth number : "))
        no5 = int(input("Enter the fifth number : "))

    maximum(no1, no2, no3, no4, no5)

if __name__ == "__main__" :
    main()