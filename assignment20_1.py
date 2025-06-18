from sys import argv
import hashlib
import os

def dicrectory(value = "demo") :
    ret = os.path.isabs(value)

    if ret == False :
        value = os.path.abspath(value)

    ret = os.path.exists(value)

    if ret == False :
        print("path dont exist")
        exit()

    ret = os.path.isdir(value)

    if ret == False :
        print("input is file")
        exit()

    for foldername, subfoldernames, filenames in os.walk(value) :
        for fname in filenames:
            ret = os.path.join(foldername, fname)
            checksum(fname)

def checksum(value) :
    fobj = open(value, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(1024) 

    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    fobj1 = open("assignment20.log", "a")

    fobj1.write("--------------------------------------------------------------------------------")
    fobj1.write("assignment20_1\n")
    ret = ("check sum of %s is %s:"%(value, hobj.hexdigest()))
    fobj1.write(ret)

    fobj1.close()

def main() :
    if len(argv) == 2 :

        if (argv[1] == "--h") or (argv[1] == "--H"):
            print("this program is use to find the check sum of files in given directory")

        elif (argv[1] == "--u") or (argv[1] == "--U") :
            print("enter directory name ")

        dicrectoyname = argv[1]

        dicrectory(dicrectoyname)

    else :
        print("invalid number of input")
        print("this program accept 2 input")
        print("this program is use to find the check sum of files in given directory")

if __name__ == "__main__" :
    main()