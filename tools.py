import smtplib
import ssl
from email.message import EmailMessage


def send_mail(sender, password, receiver, subject, body):
    # Define email sender and receiver
    email_sender = sender
    email_password = password
    email_receiver = receiver

    # Set the subject and body of the email
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        print(f"sending message: {body}")
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


