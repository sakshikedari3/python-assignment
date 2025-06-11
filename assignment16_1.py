def main() :
   obj = open("student.txt", "w")

   name1 = input("enter 1st name : ")
   obj.write(name1+"\n")

   name2 = input("enter 1st name : ")
   obj.write(name2+"\n")

   name3 = input("enter 1st name : ")
   obj.write(name3+"\n")

   name4 = input("enter 1st name : ")
   obj.write(name4+"\n")

   name5 = input("enter 1st name : ")
   obj.write(name5+"\n")

   obj.close()

if __name__ == "__main__" :
    main()
    
