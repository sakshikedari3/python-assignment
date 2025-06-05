class student :
    school_name = "Pune Vidyarthi Griha"
    def __init__(self, a, b, c):
        self.name = a
        self.roll_no = b
        student.school_name = c

    def display(self) :
        print("name of student is :",self.name)
        print("roll-no is :",self.roll_no)
        print("name of school is :",student.school_name)

def main () :
    name = input("enter your name : ")
    roll_no = int(input("enter your roll no : "))
    school = input("enter school name : ")

    obj = student(name, roll_no, school)

    obj.display()

if __name__ == "__main__" :
    main()
