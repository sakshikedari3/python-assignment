import os
import sys 
import time
import hashlib 

def calculateCheckSum(path, blockSize = 1024) :

    fobj = open(path, 'rb') 

    hobj = hashlib.md5()

    buffer = fobj.read(blockSize)
    while len(buffer) > 0 :
        hobj.update(buffer) 
        buffer = fobj.read(blockSize)

    fobj.close()

    return hobj.hexdigest()

def dicrectoryWatcher(Directoryname = "marvolus") :

    flag = os.path.isabs(Directoryname)

    if flag == False :
        Directoryname = os.path.abspath(Directoryname)

    flag = os.path.exists(Directoryname) #check path exists

    if flag == False :
        print("path is invalid")
        exit()

    flag = os.path.isdir(Directoryname) #check name is directoey

    if flag == False :
        print("path is valid but the target is not directory")
        exit()

    for foldername, SumFoldernames, FileNames in os.walk(Directoryname) :

        for fname in FileNames :
            fname = os.path.join(foldername, fname)

            checksum = calculateCheckSum(fname)
            print("filename :",fname)
            print("checkname :",checksum)
            print()
           
    timestamp = time.ctime()

    FileName = "marvoluslos%s.log" %(timestamp)

    FileName = FileName.replace(" ","_")
    FileName = FileName.replace(":","_")

    fobj = open(FileName,"w")

    border = "-" * 76

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(border)
    fobj.write("\nfile created at :"+timestamp)
    fobj.write("\n"+border+"\n")

def findDuplicate(Directoryname = "marvolus") :

    flag = os.path.isabs(Directoryname)

    if flag == False :
        Directoryname = os.path.abspath(Directoryname)

    flag = os.path.exists(Directoryname) #check path exists

    if flag == False :
        print("path is invalid")
        exit()

    flag = os.path.isdir(Directoryname) #check name is directoey

    if flag == False :
        print("path is valid but the target is not directory")
        exit()

    duplicate = {}

    for foldername, SumFoldernames, FileNames in os.walk(Directoryname) :

        for fname in FileNames :
            fname = os.path.join(foldername, fname)

            checksum = calculateCheckSum(fname)
            
            if checksum in duplicate :
                duplicate[checksum].append(fname)

            else :
                duplicate[checksum] = [fname]

    return duplicate

def displayresult(myDict):
    result = list(filter(lambda x : len(x) > 1, myDict.values()))

    count = 0

    for value in result :
        for subvalue in value :
            count += 1
            print(subvalue)
        print("----------------------------")
        print("value of count is :",count)
        print("----------------------------")
        count = 0

def deleteDuplicate(myDict):
    result = list(filter(lambda x : len(x) > 1, myDict.values()))

    count = 0

    for value in result :
        for subvalue in value :
            count += 1
            if count > 1 :
                os.remove(subvalue)
        count = 0
            
def main() :
    border = "-" * 76
    print(border)
    print("---------------------------Marvellous automation----------------------------")
    print(border)

    if len(sys.argv) == 2:

        if ((sys.argv[1]) == "--h") or ((sys.argv[1]) == "--H") :
            print("this application is used to performed directory cleaning")
            print("this is the automation script")

        elif ((sys.argv[1]) == "--u") or ((sys.argv[1]) == "--U") :
            print("use the given script as ")
            print("script name.py name of directory")
            print("please provide valid absolute path")

        else :
            fileName = sys.argv[1]

            ret = findDuplicate(fileName)

            deleteDuplicate(ret)
    else :
        print("Invalid number of command line arguments")
        print("Use the given flag as ")
        print("--h: used to display the help")
        print("--u: used to diplay the usage")

    dicrectoryWatcher(fileName)
    displayresult(ret)

    print(border)
    print("-------------------------Thank you for using script-------------------------")
    print("---------------------------Marvellous infosys-------------------------------")
    print(border)

if __name__ == "__main__" :
    main()
