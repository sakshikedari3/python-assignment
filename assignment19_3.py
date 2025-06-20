import os
import sys
import shutil

def copy(value1, value2):
    ret = os.path.exists(value1) 
    if ret == False :
        print("directory dont exists!!")
        exit()

    ret = os.path.isdir(value1) 

    if ret == False :
        print("input is file!!")
        exit()

    ret = os.path.exists(value2) 

    if ret == True :
        print("directory already exists!!")
        exit()

    os.mkdir(value2)

    for foldername, subfolders, files in os.walk(value1) :
        for fname in files :
            shutil.copy(os.path.join(foldername, fname), value2)

            
    print("file copied successfully !!")

def main () :
    if len(sys.argv) == 3:

        dic1 = sys.argv[1]
        dic2 = sys.argv[2]

    elif len(sys.argv) == 1:
        dic1 = input("enter directory name : ")
        dic2 = input("enter the name of dictory in which you what to copy files : ")

    else :
        print("invalid number of input !!")
        exit()

    copy(dic1, dic2)

if __name__ == "__main__" :
    main()