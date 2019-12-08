import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def passwordencrpt(password):
    encrptpswd = base64.b64encode(bytes(password, 'utf-8'))
    return encrptpswd

def emailsend(sender_email,password,subject,content,receiver_email, replyTo_email):

    encrptpassword = passwordencrpt(password)
    pswd = base64.b64decode(encrptpassword)
    a = str(pswd).strip('b')
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, a.strip("'"))

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message['reply-to'] = replyTo_email
    message["Subject"] = subject
    text = content

    message.attach(MIMEText(text,'plain'))


    server.send_message(message)
