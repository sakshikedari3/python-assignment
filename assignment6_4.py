#factorial
import sys

def factorial(value) :
    a = 1
    for i in range(value, 1, -1) :
        a *= i

    print("factorial of ",value," is ",a)

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    factorial(no)

if __name__ == "__main__" :
    main()