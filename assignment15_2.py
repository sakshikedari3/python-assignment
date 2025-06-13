def file(value) :
    obj = open(value, "r")

    ret = obj.read()

    print(ret)

def main() :
    filename = input("enter file name : ")

    file(filename)

if __name__ == "__main__" :
    main()