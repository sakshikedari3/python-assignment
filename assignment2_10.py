import sys

def add(value) :
    result = 0
    for num in value :
        result += int(num)

    return result

def main():
    if len(sys.argv) > 2 :
        print("Error while accepting inputs")
        print("Press --h for help or --u for usage")
        return
    
    if len(sys.argv) == 2 :
        
        if sys.argv[1] == "--h" :
            print("this program is use to add the given number")
            return

        if sys.argv[1] == "--u" :
            print("You can enter number on command line directly or at the time of executing code")
            return
        
        no = sys.argv[1]

    else :
        no = input("Enter the number : ")

    #add(no)

    result = add(no)

    print("Sum of given number is : ",result)
    

if __name__ == "__main__" :
    main()