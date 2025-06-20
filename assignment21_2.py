import psutil
import sys

def Process(name) :
    for proc in psutil.process_iter(['name','pid','username']) :
        if proc.info['name'] == name :
            return proc.info
    exit()

def main() :
    if len(sys.argv) == 2:

        name = sys.argv[1]

    elif len(sys.argv) == 1:
        name = input("enter name of process : ")

    else :
        print("invalidnumber of input!!")
        exit()

    fobj = open("assignment21_2.txt", 'w')

    ret = Process(name)

    fobj.write(str(ret))

    fobj.close()

if __name__ == "__main__" :
    main()