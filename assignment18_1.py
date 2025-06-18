import os
import sys

def check(value) :
    ret = os.path.exists(value)

    if ret == False :
        print("directory is not present")
    
    else :
        print("directory is present")

def main() :
    try :
        if len(sys.argv) == 2 :
            if sys.argv == "--h" or sys.argv == "--H":
                print("this program is use to find the directory in presend folder")

            elif sys.argv == "--u" or sys.argv == "--U" :
                print("enter directory name")
            directory = sys.argv[1]

        elif len(sys.argv) == 1:
            directory = input("enter directory name : ")

    except  UnboundLocalError as ule:
        print("invalid number of argument", ule)
        
    check(directory)

if __name__ == "__main__" :
    main()