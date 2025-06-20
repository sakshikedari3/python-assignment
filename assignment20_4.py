import sys
import os
import hashlib
import datetime

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
        print("directory dont exists !!")
        exit() 

    ret = os.path.isdir(value)

    if ret == False :
        print("input is file!!")
        exit()

    data = {}

    for foldername, subfolders, files in os.walk(value) :

        for fname in files :
            fname = os.path.join(foldername, fname)

            checksum = CalculateCheckSum(fname)

            if checksum in data :
                data[checksum].append(fname)

            else :
                data[checksum] = [fname]

    return data

def DeleteDuplicate(value) :
    result = list(filter(lambda x : len(x) > 1, value.values()))

    fobj = open("assignment20_4.txt", "w")

    count = 0

    cnt = 0

    for files in result :
        for subfiles in files :
            count += 1
            if count > 1 :
                cnt += 1
                fobj.write("\nfile deleted : ")
                fobj.write(subfiles)
                os.remove(subfiles)
        count = 0

    fobj.write("\ntotal files deleted : ")
    fobj.write(str(cnt))

def main() :
    if len(sys.argv) == 2 :
        direct = sys.argv[1]

    elif len(sys.argv) == 1 :
        direct = input("enter name of directory : ")

    else :
        print("invalid number of input!!")
        exit()

    start_time = datetime.datetime.now()

    ret = findDuplicate(direct)

    DeleteDuplicate(ret)

    end_time = datetime.datetime.now()

    fobj = open("assignment20_4.txt", 'a')

    total_time = end_time - start_time

    fobj.write("\ntotal time needed for excutation is : ")

    fobj.write(str(total_time))

    fobj.close()

if __name__ == "__main__" :
    main()