import smtplib


def email_function(message):
    TO = ['eladnm07@gmail.com']
    CC = ['gadi5nm@gmail.com']
    SUBJECT = message
    TEXT = 'Here is a message from python.'

    # Gmail Sign In
    gmail_sender = 'eladnm07@gmail.com'
    gmail_passwd = 'qafj ukwg nngv hksk'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

try:
    server.sendmail(gmail_sender,(TO+CC), BODY)
    print('sent')
except:
    print ('error sending mail')