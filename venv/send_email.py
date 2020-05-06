from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def main():
    try:
        msg = MIMEMultipart()

        msg['from'] = 'from'
        msg['To'] = 'to'
        msg['Subject'] = 'Subject'

        message = 'hello! this is my first email from Python Script'
        msg.attach(MIMEText(message))

        #start SMTP server

        smtp = smtplib.SMTP(host ='smtp.gmail.com', port=587) #Android
        smtp.starttls()
        smtp.login('from', 'password')

        smtp.send_message(msg)

        print('Email has been sent successfully')
    except Exception as exp:
        print("Unable to  send email : {0}".format(repr(exp)))

if __name__ == '__main__':
    main()