import sys
import os
import psutil

def check (value) :
    ret = os.path.exists(value)

    if ret == False :
        print("directory dont exists!!")
        exit()

    ret = os.path.isdir(value) 

    if ret == False :
        print("input is file!!")
        exit()

    ret = os.path.isabs(value)

    if ret == False :
        value = os.path.abspath(value)

    fobj = os.path.join(value, "assignment21_3.txt")

    fobj = open("assignment21_3.txt", 'w')

    for proc in psutil.process_iter(['username','name','pid']):

        fobj.write(str(proc))
        fobj.write("\n")

    fobj.close()


def main() :

    if len(sys.argv) == 2 :
        name = sys.argv[1]

    elif len(sys.argv) == 1 :
        name = input("enter the name of directory : ")

    check(name)
    
if __name__ == "__main__" :
    main()