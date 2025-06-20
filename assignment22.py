import hashlib
import os
import sys
import time
import datetime
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def gmail(value, path, Time, Tcount, cnt) :
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    from_add = "kedarisakshi03@gmail.com"
    password = "rkzsdkzofxvsgzrx"

    subject = "to send email using python"
    body = body = (
    f"Starting time of scanning: {Time}\n"
    f"Total number of files scanned: {Tcount}\n"
    f"Duplicate files found: {cnt}"
    )

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = value
    msg['subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    file = open(path, 'rb')
    attachment = MIMEApplication(file.read(), _subtype = "txt")
    attachment.add_header('content-disposition','attachment', filename = os.path.basename(path))
    msg.attach(attachment)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_add, password)
    server.sendmail(from_add, value, msg.as_string())
    server.quit()

def CalculateCheckSum(value) :
    fobj = open(value, 'rb')

    hobj = hashlib.md5()

    buffer = fobj.read(1024)

    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(value) : 

    ret = os.path.exists(value)
    if ret == False:
        print("directory does not exist")
        os.mkdir(value)

    ret = os.path.isdir(value)
    if ret == False:
        print("input is not a directory")
        exit()

    ret = os.path.isabs(value)
    if ret == False:
        value = os.path.abspath(value)

    data = {}

    for foldername, subfolders, files in os.walk(value) :
        for fname in files :
            fname = os.path.join(foldername, fname)

            checksum = CalculateCheckSum(fname)

            if checksum in data :
                data[checksum].append(fname)

            else :
                data[checksum] = [fname]

    return data

def deleteDuplicate(value) :
    data = FindDuplicate(value)

    result = list(filter(lambda x : len(x) > 1, data.values()))

    count = 0
    cnt = 0

    timestamp = time.ctime()

    fileName = "marvoluslos%s.log" %(timestamp)

    fileName = fileName.replace(" ","_")
    fileName = fileName.replace(":","_")

    logPath = os.path.join(value, fileName)

    fobj = open(logPath, 'w')

    for files in result :
        for subfile in files :
            count += 1
            if count > 1 :
                cnt += 1
                fobj.write(subfile)
                fobj.write("\n")
                os.remove(subfile)

        count = 0

    fobj.write("\nnumber of total file deleted : ") 
    fobj.write(str(cnt))

    fobj.close()

    return count, cnt, logPath

def main() :
    if len(sys.argv) == 4:
        file = sys.argv[1]
        duration =sys.argv[2]
        email = sys.argv[3]

    elif len(sys.argv) == 1:
        file = input("enter the name of directory : ")
        duration = int(input("enter the time : "))
        email = input("enter email id you want to send mail to : ")

    else :
        print("invalid number of inputs!!")
        exit()

    startTime = datetime.datetime.now()

    count, cnt, logpath = deleteDuplicate(file)

    gmail(email, logpath, startTime, count, cnt)

    schedule.every(duration).minutes.do(deleteDuplicate, file)

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()