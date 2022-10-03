import smtplib
from email.message import EmailMessage
from string import Template
import os


def apmokek(kreipinys, elpastas, suma):
    with open('skola.html', 'r', encoding="utf8") as f:
        html = f.read()

    sablonas = Template(html)

    email = EmailMessage()
    email['from'] = 'Skolos administratorius'
    email['to'] = 'testmailcodeacademy@gmail.com'
    email['subject'] = 'Pranešimas apie įsiskolinimą'

    email.set_content(sablonas.substitute(
        {'kreipinys': kreipinys,
         'skola': suma,
         'mail': elpastas}),
        'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('testas2.testuotas@gmail.com', "jipxvwukqowwcmry")
        smtp.send_message(email)


apmokek('Antanai', 'mykolas174@gmail.com', 25.25)
