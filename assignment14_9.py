class product :
    def __init__ (self, a, b) :
        self.name = a
        self.price = b

    def __eq__ (self, other) :
        return self.price == other.price 
        
def main() :
    p1 = product("book", 670)
    p2 = product("pencile", 20)
    p3 = product("pen", 20)

    print(p1 == p2)
    print(p1 == p3)
    print(p2 == p3)

if __name__ == "__main__" :
    main()
