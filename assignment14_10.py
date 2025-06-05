class employee :
    def __init__(self, a, b, c) :
        self.name = a   
        self._department = b 
        self.__salary = c

    def display(self) :
        print("inside employee class")
        print(self.name)
        print(self._department)
        print(self.__salary) 

    def get_class (self) :
        return self.__salary
    
def main() :

    obj = employee('rahul', "it", 896500)
    obj.display()
    ret= obj.get_class()

    print("inside main class")
    print(obj.name)
    print(obj._department)

    print(ret)

if __name__ == "__main__" :
    main()