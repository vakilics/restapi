#Note: login to google account -> manage account -> security -> under 2-factor... -> create app password
import smtplib,ssl
import os

def tomail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "vakilitestmail@gmail.com"
    #password = "dfr jrxeomykkolvyzoa sdf"  #NOTE: not secure! so store it in environment variable!
    password = os.getenv("PASSW")

    receiver = "hamidgml@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)