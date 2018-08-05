import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mass_email(subject, heading, body, password, mail_list):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "sabercatrobotics@gmail.com"

    html = open("test_template.html").read()
    html = html.replace("{{body}}", body)
    html = html.replace("{{heading}}", heading)

    msg.attach(MIMEText(html, 'html'))
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login("sabercatrobotics@gmail.com", password)
    
    for email_address in mail_list:
        email_address = email_address.rstrip()
        msg['To'] = email_address
        server.sendmail("sabercatrobotics@gmail.com", email_address, msg.as_string())
    server.close()