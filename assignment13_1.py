class bookstore :
    NoOfBooks = 0
    def __init__ (self, a, b):
        self.name = a
        self.author = b
        bookstore.NoOfBooks += 1

    def display(self) :
        print("name of book is",self.name,"by",self.author,"no of books are :",bookstore.NoOfBooks)

def main():
    obj1 = bookstore("linux system programming","robert love")
    obj1.display()
    
    obj2 = bookstore("c programming","dinnie ritchie")
    obj2.display()

if __name__ == "__main__" :
    main()
    