import schedule
import time

def display() :
    print("do coding ....")

def main() :
    schedule.every(30).minutes.do(display)

    print("program is n wating state... ")

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()