#!/usr/bin/env python
# coding: utf-8

# In[12]:


# In this example, you first define HTML message as string literals, and then store them as html MIMEText objects. These can then be added in this order to the MIMEMultipart("html") message and sent through your secure connection with the email server.

# Adding Attachments Using the email Package

# In order to send binary files to an email server that is designed to work with textual data, they need to be encoded before transport. This is most commonly done using base64, which encodes binary data into printable ASCII characters.

# The code example below shows how to send an email with a PDF file as an attachment:

import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailsendattach(sender_email,receiver_email,subject,password,content,attachment):
    subject = subject
    sender_email = sender_email
    receiver_email = receiver_email
    password = password

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    html = f'''
    <html>
      <body>
        <p>Hi,<br>
           <p>{content}</p>
           Please find the attached file <br>
           <a href="https://masterdatascience.science.ubc.ca">Master in Data Science</a>
        </p>
      </body>
    </html>
    '''


    # Add body to email
    message.attach(MIMEText(html, "html"))

    filename = attachment # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
