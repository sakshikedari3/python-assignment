import sys
import os

def check(value1, value2) :
    ret = os.path.exists(value1)

    if ret == False :
        print("dictory dont exists")
        exit()

    ret = os.path.isdir(value1)

    if ret == False :
        print("input is file")
        exit()

    for foldername, subfolders, files in os.walk(value1) :
        for fname in files :
            if fname.endswith(value2):
                print(fname)

def main() :
    if len(sys.argv) == 3 :
        name = sys.argv[1]
        extension = sys.argv[2]

    elif len(sys.argv) == 1:
        name = input("Enter dicrectory name : ")
        extension = input("enter extension : ")

    check(name,extension)

if __name__ == "__main__" :
    main()