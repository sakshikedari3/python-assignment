#even or odd
import sys

def chknum(value) :
    if value % 2 == 0 :
        print("Number is even")

    else :
        print("Number is odd")

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    chknum(no)

if __name__ == "__main__" :
    main()