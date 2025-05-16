#pattern *
import sys

def pattern(value) :
    for _ in range(value) :
        print("*" * value)

def main():
    if len(sys.argv) > 2 :
          print("Error while accepting inputs")
          print("Press --h for help or --u for usage")
          return
     
    if len(sys.argv) == 2 :
        if sys.argv[1] == "--h" :
              print("this program is use to get pattern of star(*)")
              return

        if sys.argv[1] == "--u" :
              print("You can add number on command line directly or at the time of executing code to get output")
              return
        no = int(sys.argv[1])

    else :
        no = int(input("Enter the number : "))

    pattern(no)

if __name__ == "__main__" :
    main()