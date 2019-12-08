
# **webcommunication** Package
The webcommunication package is used to establish a connection with varieties of cloud-based communication platform which allows the user to interact with them in Python
######  **webcommunication** Package contains two subpackages: `slack` and `email`.

## slack Subpackage
###### slack subpackage contains two modules: `slackchannel` and `slackmessage`.
### slackchannel.py
-This module uses Slack API (Application Programming Interface), which is used to communicate Slack with Python
- Using `slackchannel` module, the user can establish a connection with Slack and create a private channel using Python.
-This module has one class  `slackChannel` with two functions `connection` and `createchannel`.
-This module uses `import slack` to access Slack from Python.

`connection` function is used to create a connection with Slack before creating a channel.
* This module uses a slack function `WebClient`, which has parameters that needs to be passed in order to connect Slack with Python. The user will pass a token (the token can be generated from Slack API) to establish a connection.

`createchannel` function helps the user can create a private channel once a connection has been made.
* This function has one parameter, which is the name of the channel.
-When this is called, it automatically connects the user and creates a private channel.
-Slack function `groups_create` creates a private channel for the user.

### slackmessage.py
- Using `slackmessage` module, the user can send a message in any channel.
- This module has two classes `slackConnect` and `slackMessage(slackConnect))` and three functions `connection`, `sendmessage`, and `scheduledmessage`.
-This module has the following modules: `import slack`, `import calendar`, `import datetime`, and `import timedelta`. Since Slack uses UNIX timestamp these modules are used to convert PST time to UNIX timestamp.

 `slackConnect`, is a super class. `slackMessage` is inherited from `slackConnect` class.
* Using `sendmessage` function, the user can input channel name, a text message, and preferred username (default is "Slack API tester")
  - Slack function `chat_postMessage` is used to send message in the user created channel.
-Using `scheduledmessage` function, the user can input channel name, a text message, and date in *yyyy-mm-ss hh-mm-ss* format.
  - Slack function `chat_scheduleMessage` is used to send message in the user created channel at a chosen time.

## email SubPackage
###### email subpackage contains two modules: `emailsimple` and `emailadvanced`
## emailsimple.py
- Using this module the user is establishes a connection and sends an email in plain text format.
- This module has two functions `passwordencript` and `emailsend`.
- Inside this module we have imported the following modules:
  - `import smtplib`, Simple Mail Transfer Protocol is needed to establish a connection between SMTP server and the host.
  - `import base64`, used for password encryption and decryption.
  - `from email.mime.multipart import MIMEMultipart`, used to specify the subtype of an email.
  - `from email.mime.text import MIMEText`, used to send email as a text/HTML attachment.

`passwordencript`, the user inputted password is encrypted using `b64encode` function.

`emailmessage` function, the user can input sender's email, password, subject, content of email, receiver's email, and reply to email.
- The password that the user inputted will access `passwordencript` function and after it's encrypted, it is decrypted using `b64decode` function connects to the SMTP server using a specific port number.

## emailadvanced.py
- Using this module, the user can send email in HTML format with an attachment.
- Inside this module the following modules are imported:
  - `import smtplib`,`from email.mime.multipart import MIMEMultipart`, `from email.mime.text import MIMEText`.
  -`import email` is the main package that imports the following modules:
  - `import ssl`, the user will be able to log in to server using the secure connection.
  -`from email import encoders`,function will take the attached file and encode file in ASCII character to send by email.
  -`from email.mime.base import base`,function is converting the user attached .PDF in a binary mode.
- This module has one function `emailsendattach`

`emailsendattach` function, the user can input  sender's email, password, subject, content of email, receiver's email.
- To send a message `MIMEMultipart` function is used since the email includes an attachment.
- The text of the email is formatted in HTML format.
- A user can input a .PDF file as an attachment to the email.
- In order to attach a file, it should be located in the same directory.

#### Sneha Mikkilineni Durga, Binal Patel
