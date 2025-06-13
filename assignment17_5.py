import schedule
import datetime
import time

def display() :
    ret = open("marvolus.txt", "a")
    
    ret.write(str(datetime.datetime.now()))

def main() :
    schedule.every(5).minutes.do(display)

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()