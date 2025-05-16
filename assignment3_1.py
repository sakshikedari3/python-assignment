import sys

def add(value) :
    for n in value :
        sum += n
    return sum
def main():
    if len(sys.argv) > 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    data = []
    
    if len(sys.argv) > 2 :

        if sys.argv[1] == "--h" :
            print("this program is use to addition of given number in list")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
    
        data = list(map(int, sys.argv[1:]))

    else :
        size = int(input("Enter the number of element you want to enter : ")) 

        for _ in range(size) :
            a = int(input("Enter the element : "))
            data.append(a)

    result = sum(data)

    print("Result is : ",result)

if __name__ == "__main__" :
    main()