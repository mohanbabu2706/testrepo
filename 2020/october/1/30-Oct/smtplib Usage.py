"""The first step is to create an SMTP object,each object is used with one swith one server"""

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

#Next,log in to the server
server.login("youremailusername","password")

#send the email
msg = "Hello!"
#The /n separates the message from the headers
server.sendmail("you@gmail.com","target@example.com",msg)
