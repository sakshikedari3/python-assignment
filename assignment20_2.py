import os
import sys
import hashlib

def calculateCheckSum(path, blocksize = 1024):

    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()


def duplicate(value1) :
    ret = os.path.exists(value1)

    if ret == False:
        print("directory does not exist!!")
        exit()

    ret = os.path.isdir(value1)

    if ret == False :
        print("input is not a directory!!")
        exit()

    data = {}

    for foldername, subfoldernames, files in os.walk(value1):
        for fname in files :
            fname = os.path.join(foldername, fname)
            checksum = calculateCheckSum(fname)

            if checksum in data:
                data[checksum].append(fname)

            else :
                data[checksum] = [fname]

    return data

def main() :
    if len(sys.argv) == 2 :
        file = sys.argv[1]

    elif len(sys.argv) == 1 :
        file = input("enter the directory name : ")

    ret = duplicate(file)

    print("list is : ",ret)

if __name__ == "__main__" :
    main()