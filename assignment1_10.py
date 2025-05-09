def length(value) :
    result = len(value)
    return result

def main():
    print("Enter your name :  ")
    name = input()
    result = length(name)
    
    print("Length of your name is : ",result)

if __name__ == "__main__" :
    main()