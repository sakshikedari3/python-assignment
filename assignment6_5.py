#prime number
import sys

def prime(value) :
    for i in range(2, value) :
        if value % i == 0:
            return False
        
        else :
            return True

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    result = prime(no)

    if result :
        print("Number is prime")

    else :
        print("Number is not prime")

if __name__ == "__main__" :
    main()