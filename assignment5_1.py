#arithmatic operations
import sys

def add(no1, no2) :
    return no1 + no2

def sub(no1, no2) :
    return no1 - no2

def multiply(no1, no2) :
    return no1 * no2 

def div(no1, no2) :
    return no1 / no2

def main () :
    if len(sys.argv) == 4 :
        no1 = int(sys.argv[1])
        no2 = int(sys.argv[2])
        no3 = sys.argv[3]

    else :
        no1 = int(input("Enter the first number : "))
        no2 = int(input("Enter the second number : "))
        no3 = input("Which opreation you have to perform\n1. add\n2. sub\n3. multiply\n4. div\n5. all \n")

    if no3 == "add" or no3 == "1" or no3 == "+" :
        print(add(no1, no2))

    elif no3 == "subtract" or no3 == "2" or no3 == "-" :
        print(sub(no1, no2))

    elif no3 == "multiply" or no3 == "3" or no3 == "*" :
        print(multiply(no1, no2))

    elif no3 == "divide" or no3 == "4" or no3 == "/" :
        print(div(no1, no2))

    elif no3 == "all" or no3 == "5" :
        print("addition is : ",add(no1, no2))
        print("subtraction is : ",sub(no1, no2))
        print("multiplaction is : ",multiply(no1, no2))
        print("division is : ",div(no1, no2))

    else :
        print("Invalid choice")

if __name__ == "__main__" :
    main()