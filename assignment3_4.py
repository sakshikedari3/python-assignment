import sys

def frequency(value1, value2) :
    a = 0
    for n in value1 :
        if n == value2:
            a += 1
    return a

def main():
    if len(sys.argv) == 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    data = []
    
    if len(sys.argv) > 2 :

        if sys.argv[1] == "--h" :
            print("this program is use to return frequency of given number in list")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
    
        no = int(sys.argv[1])
        data = list(map(int, sys.argv[2:]))

    else : 
        no = int(input("enter the number you want to find frequency of : "))
        size = int(input("Enter the number of elements you want to enter : "))

        for _ in range(size) :
            a = int(input("Enter the element : "))
            data.append(a)

    result = frequency(data, no)

    print("In data",data,"," ,no,"Number has frequency :",result)

if __name__ == "__main__" :
    main()