import os
import sys

def check(value) :
    ret = os.path.exists(value)

    if ret == True :

        ret = os.path.isfile(value)

        if ret == True :
            a = open(value, "r")

            data = a.read()

            print(data)

        else :
            print("input is directory")

    else :
        print("file dont exists")

def main() :
    if len(sys.argv) == 1 :
        file = input("enter file name : ")

    elif len(sys.argv) == 2:
        file = sys.argv[1]

    else :
        print("invalid number of input")

    check(file)

if __name__ == "__main__" :
    main()