import sys

def display(value1, value2) :
    obj1 = open(value1, "r")

    data1 = obj1.read()

    obj2 = open(value2, "r")

    data2 = obj2.read()

    if data1 == data2 :
        print("success")

    else :
        print("failur")

def main() :
    if len(sys.argv) == 3 :
        file1 = sys.argv[1]
        file2 = sys.argv[2]

    elif len(sys.argv) == 1 :
        file1 = input("enter first file name : ")
        file2 = input("enter second file name : ")

    display(file1, file2)

if __name__ == "__main__" :
    main()