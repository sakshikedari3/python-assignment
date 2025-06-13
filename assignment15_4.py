import sys

def file(value1, value2) :
    obj1 = open(value1, "r")

    data1 = obj1.read()

    obj2 = open(value2, "r")

    data2 = obj2.read()

    if data1 == data2 :
        print("success")

    else :
        print("failure")

def main () :

    if len(sys.argv) == 3 :

        filename1 = sys.argv[1]
        filename2 = sys.argv[2]

    file(filename1, filename2)

if __name__ == "__main__" :
    main()
