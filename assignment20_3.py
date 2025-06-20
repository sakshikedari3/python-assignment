import os
import sys
import hashlib

def CalculateCheckSum(value) :
    fobj = open(value, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def findDuplicate(value) :
    ret = os.path.exists(value)

    if ret == False :
        print("directroy dont exists!!")
        exit()

    ret = os.path.isdir(value)

    if ret == False :
        print("input is file!!")
        exit()

    data = {}

    for foldername, subfolders, files in os.walk(value) :
        for fname in files :
            fname = os.path.join(foldername, fname)
            ret = CalculateCheckSum(fname)

            if ret in data :
                data[ret].append(fname)

            else :
                data[ret] = [fname]

        return data

def deleteDuplicate(value) :
    result = findDuplicate(value)

    ret = list(filter(lambda x : len(x) > 1, result.values()))

    fobj = open("log.txt",'w')

    count = 0
    cnt = 0

    for file in ret:
        for subfile in file :
            count += 1
            if count > 1 :
                cnt += 1
                fobj.write(subfile+"\n")
                os.remove(subfile)

        count = 0

    fobj.write("\ntotal files deleted : ")
    fobj.write(str(cnt))

def main() :
    if len(sys.argv) == 2:
        filename = sys.argv[1]

    elif len(sys.argv) == 1 :
        filename = input("enter name of directory : ")

    else :
        print("invalid number of argument : ")
        exit()

    deleteDuplicate(filename)

if __name__ == "__main__" :
    main()