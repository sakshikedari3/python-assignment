import os
import psutil

def display() :
    fobj = open("assignment21_1.txt","w")

    for proc in psutil.process_iter() : #same as os.walk
        info = proc.as_dict(attrs=['pid', 'name', 'username'])
        fobj.write(str(info))

    fobj.close()

def main() :
    display()

if __name__ == "__main__" :
    main()