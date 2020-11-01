from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "you@gmail.com"
toaddr = "target@example.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

body = "Python test mail"
msg.attach(MIMEText(body,'plain'))

import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.startls()
server.ehlo()
server.login("youremailusername","password")
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
