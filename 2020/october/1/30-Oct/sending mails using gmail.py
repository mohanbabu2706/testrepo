import smtplib

def sendmail(from_addr,to_addr_list,cc_addr_list,
             subject,message,
             login,password,
             smtpserver = 'smtp.gmail.com:587'):
    header = 'From: %s
' % from_addr
    header += 'To: %s
'%','.join(to_addr_list)
    header += 'Cc:%s
'%','.join(cc_addr_list)
    header += 'Subject:%s
'% subject

message = header + message

server = smtplib.SMTP(smtpserver)
server.starttls()
server.login(login,password)
problems = server.sendmail(from_addr,to_addr_list,message)
server.quit()

#Example Usage of above script

sendmail(from_addr = 'python@RC.net',
         to_addr_list = ['RC@gmail.com'],
         cc_addr_list = ['RC@xx.co.uk']
         subject = 'Howdy',
         message = 'Howdy from a python function',
         login = 'pythonuser',
         password = 'xxxx')

#Sample Email Recieved

sendmail(from_addr = 'python@RC.net',
         to_addr_list = ['RC@gmail.com'],
         cc_addr_list = ['RC@xx.co.uk'],
         subject = 'Howdy',
         message = 'Howdy from a python function',
         login = 'pythonuser',
         password = 'XXXX')
