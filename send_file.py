import sys, smtplib
from secret_settings import gmail_account, gmail_password, default_reciever
from email import Encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase

import os

class Email():
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.login(gmail_account, gmail_password)
       
    def send(self, reciever, filename):
        if not reciever:
            reciever = default_reciever
        msg = MIMEMultipart()
        msg['From'] = gmail_account
        msg['To'] = reciever
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(filename,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 
                        'attachment; filename="%s"' % os.path.basename(filename).encode('utf8') )
        msg.attach(part)
        self.mailServer.sendmail(gmail_account, reciever, msg.as_string())

email = Email()
email.send(None, sys.argv[1])
