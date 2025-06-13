import schedule
import time

def display() :
    print("jay ganesh")

def main() :
    schedule.every(2).seconds.do(display)

    print("progrem is at wating state...")

    while True :
        schedule.run_pending()
        time.sleep(1) 

if __name__ == "__main__" :
    main()