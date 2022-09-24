from email.mime.text import MIMEText
from mimetypes import MimeTypes
import smtplib

def send_email(email, height, average_height, count):
    # from_email = "admin@filippeszke.pl"
    from_email = "filiptest880@gmail.com"
    # from_password = "NGIfermi2%f1"
    from_password = "pythonlecture"
    to_email = email

    subject = "Height data"
    message = "Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people." % (height, 
    average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    
    # host = smtplib.SMTP('filippeszke.pl', 587)
    host = smtplib.SMTP('smtp.gmail.com', 587)
    host.ehlo()
    host.starttls()
    host.login(from_email, from_password)
    host.send_message(msg)