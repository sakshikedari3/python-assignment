import schedule
import time
import datetime
import os

def display() :
    ret = open("backup_log.txt", "a")
    ret.write(str("filebackup successfull at :",datetime.datetime.now()))

def main() :
    schedule.every(1).hour.do(display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()


    