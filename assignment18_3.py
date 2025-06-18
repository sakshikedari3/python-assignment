import sys

def create(value) :
    robj = open(value, "r")

    data = robj.read()

    robj.close()

    fobj = open("demo.txt", "w")

    fobj.write(data)

    fobj.close()

    print("content copied successfull")

def main() :
    if len(sys.argv) == 1 :
        file = input("Enter the name of file which you want to copy : ")

    elif len(sys.argv) == 2 :
        file = sys.argv[1]

    else :
        print("inalid number of inputs")

    create(file)

if __name__ == "__main__" :
    main()
