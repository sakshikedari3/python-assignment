class vehicle :
    def start(self) :
        print("inside the vehicle class")

class car (vehicle) :
    def start(self) :
        print("inside car class")
        print("this function override vehicle class")

def main() :

    vobj = vehicle()
    cobj = car()

    vobj.start()
    cobj.start()

if __name__ == "__main__" :
    main()

