from email.mime.text import MIMEText
import smtplib 
import secrets

def send_email(email, data_number):
    from_email="patundmaz@gmail.com"
    from_password=secrets.get_password()
    to_email=email

    message=MIMEText("You send number <strong>%s</strong>." % data_number, 'html')
    message['Subject']="mailing test"
    message['To']=to_email
    message['From']=from_email

    wp=smtplib.SMTP('smtp.gmail.com', 587)
    wp.ehlo()
    wp.starttls()
    wp.login(from_email, from_password)
    wp.send_message(message)