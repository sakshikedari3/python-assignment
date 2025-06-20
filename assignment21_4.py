import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import sys
import os
import psutil

def check(value):
    ret = os.path.exists(value) 

    if ret == False:
        print("directory dont exists")
        os.mkdir(value)

    ret = os.path.isdir(value) 

    if ret == False:
        print("input is file!!")
        exit()

    ret = os.path.isabs(value)

    if ret == False:
        value = os.path.abspath(value)

    fobj = os.path.join(value, "assignment21_4.txt")

    with open(fobj, 'w') as fobj:
        for proc in psutil.process_iter(['username', 'name', 'pid']):
            fobj.write(str(proc)) 
            fobj.write("\n")
    
    return fobj

def gmail(value, file_path):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    from_add = "kedarisakshi03@gmail.com"
    password = "rkzsdkzofxvsgzrx" 

    subject = "test email from python"
    body = "hello! this is mail which im sending using python"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = value
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    file = open(file_path, 'rb')
    attachment = MIMEApplication(file.read(), _subtype="txt")
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file_path))
    msg.attach(attachment)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_add, password)
    server.sendmail(from_add, value, msg.as_string())
    server.quit()

    print("email sent successfully")

def main():
    if len(sys.argv) == 3:
        file = sys.argv[1]
        email = sys.argv[2]

    elif len(sys.argv) == 1:
        file = input("enter the name of directory : ")
        email = input("enter email address : ")

    else:
        print("invalid input!!")
        exit()

    path = check(file)

    gmail(email, path)

if __name__ == "__main__":
    main()