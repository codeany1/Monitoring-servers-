import smtplib
from email.message import EmailMessage

def email_alert(subject, body, to):

    msg = EmailMessage()
    msg.set_content(body)

    # UPDATE THESE LINES TO YOUR INFO
    gmail_user = 'YourEmail@gmail.com'
    gmail_password = 'get_app_password'
    msg['Subject'] = subject
    msg['From'] = "YourEmail@gmail.com"
    msg['To'] = to


    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login(gmail_user, gmail_password)
    s.send_message(msg)
    s.quit()
