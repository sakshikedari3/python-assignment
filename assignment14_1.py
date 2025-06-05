class employee :
    def __init__(self, a, b, c):
        self.name = a
        self.id = b
        self.salary = c

    def display(self) :
        print("name :",self.name)
        print("employee id :",self.id)
        print("salary :",self.salary)

def main () :
    name = input("enter your name : ")
    id = int(input("enter your id : "))
    salary = int(input("enter your salary : "))

    obj = employee(name, id, salary)

    obj.display()

if __name__ == "__main__" :
    main()