import os

def file(value) :
    value1 = os.path.abspath(value)

    ret = os.path.exists(value1)

    if ret == True :
        print("file exists")

    else :
        print("file dont exists")

def main () :
    filename = input("enter filename : ")

    file(filename)

if __name__ == "__main__" :
    main()