#table
import sys

def table(value) :
    for a in range(1,11) :
        print(value," * ",a," = ",value*a)

def main():
    if len(sys.argv) == 2 :
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    table(no)

if __name__ == "__main__" :
    main()