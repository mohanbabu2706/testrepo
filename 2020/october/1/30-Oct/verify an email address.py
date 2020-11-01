import smtlib

server = smtplib.SMTP('mail')
server.set_debuglevel(True) #Show communication with the server

try:
    dhellmann_result = server.verify('dhellmann')
    notthere_result = server.verify('notthere')
finally:
    server.quit()

print('dhellmann:',dhellmann_result)
print('nothere:',notthere_result)
