def main() :
    obj = open("marks.txt", "w")
    obj.write("Aarav - 85\nRiya - 90  \nKabir - 78  \nAnanya - 88  \nVikram - 92  \nSneha - 80  \nRohan - 86  \nMeera - 89  \nAditya - 83  \nIshaan - 95  \nNeha - 76\n ") 
    obj.write("Siddharth - 91  \nTanvi - 72  \nRajesh - 68  \nPooja - 74  \nArjun - 65  \nPriya - 70  \nNikhil - 73  \nKomal - 62  \nVarun - 69")

    obj.close()

    obj = open("marks.txt", "r")
    data = obj.readlines()

    for a in data:
        name, marks = a.split("-")
        if int(marks) > 75 :
            print(a)

if __name__ == "__main__" :
    main()