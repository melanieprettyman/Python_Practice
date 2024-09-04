import smtplib # protocol for sending email (like http)
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['From'] = 'Melanie Prettygirl'
email['To'] = 'melanie.prettyman98@gmail.com'
email['Subject'] = 'Hello from my python project'
email.set_content(html.substitute({'name': 'Poopy head'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('all good boss!')