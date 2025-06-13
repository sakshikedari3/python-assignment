import sys

def file(value1, value2) :
    obj = open(value1, "r")

    data = obj.read()

    
    ret = data.split(" ")
    
    a = ret.count(value2)

    print("string occurence :",a)

def main () :

    if len(sys.argv) == 3 :
        filename = sys.argv[1]

        string = sys.argv[2]

    file(filename, string)

if __name__ == "__main__" :
    main()