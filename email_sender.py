########################################################################
#   Email blast script for sending formatted html emails               #
#   to a group of people individually.                                 #
#                                                                      #
#   Usage: python email_sender.py <subject> <message.html> <mail_list> #
#   (requires 'password' file in directory)                            #
#   Written by GowanR for Sabercat Robotics                            #
########################################################################


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
help_message = """
Usage: python email_sender.py <subject> <message.html> <mail_list>
"""
try:
    sys.argv[1]
    sys.argv[2]
    sys.argv[3]
except Exception:
    print help_message

username = "sabercatrobotics@gmail.com"
with open("password") as fl:
    password = fl.read().rstrip()


msg = MIMEMultipart('alternative')
msg['Subject'] = sys.argv[1]
msg['From'] = username

html = open(sys.argv[2]).read()
msg.attach(MIMEText(html, 'html'))

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(username, password)
with open(sys.argv[3]) as email_list:
    for email_address in email_list:
        email_address = email_address.rstrip()
        msg['To'] = email_address
        server.sendmail(username, email_address, msg.as_string())
server.close()
print "Success"
