import sys

def minimum(value):
    min = len(value)
    for n in value :
        if n < min :
            min = n

    return min

def main():
    if len(sys.argv) == 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    data = []
    
    if len(sys.argv) > 2 :

        if sys.argv[1] == "--h" :
            print("this program is use to minimun number of given numbers from list")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
     
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("Enter the number of elements you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the element : "))
            data.append(a)

    result = minimum(data)

    print("minimum number is :",result)

if __name__ == "__main__" :
    main()