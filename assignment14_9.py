class product :
    def __init__ (self, a, b) :
        self.name = a
        self.price = b

    def __eq__ (self, other) :
        ret =  self.price == other.price 
        if ret == True:
            return ret
        else :
            return False
        
def main() :
    p1 = product("book", 670)
    p2 = product("pencile", 20)
    p3 = product("pen", 20)

    if(p1 == p2) == True :
        print("price of product 1 and 2 are same")
    if(p1 == p3) == True :
        print("price of product 1 and 3 are same")
    if(p2 == p3) == True :
        print("price of product 2 and 3 are same")

if __name__ == "__main__" :
    main()
