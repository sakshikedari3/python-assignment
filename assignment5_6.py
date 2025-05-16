#celisus
import sys

def chk(value) :
    fer = ((value * (9/5)) + 32)
    print(fer,"F")

def main():
    if len(sys.argv) == 2 :
        temp = int(sys.argv[1])

    else :
        temp = int(input("Enter the tempreture : "))

    chk(temp)

if __name__ == "__main__" :
    main()