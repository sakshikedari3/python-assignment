import sys

def file(value) :
    obj = open("abc.txt", "r")

    data = obj.read()

    obj.close()

    obj = open(value, "w")

    obj.write(data)

    obj.close()

def main() :
    if len(sys.argv) == 2:

        filename = sys.argv[1]

    file(filename)

if __name__ == "__main__" :
    main()