import os
import sys
import shutil

def copy(value1, value2, value3) :

    ret = os.path.exists(value1)
    if ret == False:
        print("directory dont exists!!")
        exit()

    ret = os.path.isdir(value1)
    if ret == False:
        print("input is file!!")
        exit()

    ret = os.path.exists(value2)
    if ret == True:
        print("directory already exists!!")
        exit()
        
    os.mkdir(value2)
    
    for foldername, subfoldernames, files in os.walk(value1) :
        for fname in files :
            if fname.endswith(value3) :
                shutil.copy(os.path.join(foldername, fname), value2)

    print("files copied successfull!!")

def main() :
    if len(sys.argv) == 4 :
        dic1 = sys.argv[1]
        dic2 = sys.argv[2]
        extension = sys.argv[3]

    elif len(sys.argv) == 1 :
        dic1 = input("enter first directory : ")
        dic2 = input("enter second directory : ")
        extension = input("enter the extension of file you want to copy : ")

    else :
        print("invalid number of inputs !!")
        exit() 

    copy(dic1, dic2, extension)

if __name__ == "__main__" :
    main()