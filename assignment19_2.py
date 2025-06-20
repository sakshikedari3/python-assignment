import sys
import os

def change(value1, value2, value3) :

    ret = os.path.exists(value1)

    if ret == False :
        print("directory dont exist !!")
        exit() 

    ret = os.path.isdir(value1) 

    if ret == False :
        print("input is file not directory !!")
        exit() 

    for foldername, subfoldernames, files in os.walk(value1) :
        for fname in files :
            if fname.endswith(value2) :
                old_file = os.path.join(foldername, fname)
                new_file = os.path.join(foldername, os.path.splitext(fname)[0] + value3)  # new file path
                os.rename(old_file, new_file)
                print(new_file) 


def main () :
    if len(sys.argv) == 4:
        name = sys.argv[1]
        exten1 = sys.argv[2]
        exten2 = sys.argv[3]

    elif len(sys.argv) == 1:
        name = input("enter the name of directory : ")
        exten1 = input("enter extension which you want to search : ")
        exten2 = input("enter extension you want to change : ")

    else :
        print("invalid number of argument !!!")
        exit()

    change(name, exten1, exten2)

if __name__ == "__main__" :
    main()