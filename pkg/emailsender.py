import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

with open("pkg/login.json", "r") as lg:
    LG = json.load(lg)

class EmailSender:
    def __init__(self):
        self.fromaddr = LG["email_sender"]
        self.toaddr = LG["email_recipient"]
    def send(self, link):
        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = "New entry in WG-gesucht"
        body = "There is a new entry in WG-gesucht, check the files to see where the entry is" + link
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, LG['email_password'])
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()