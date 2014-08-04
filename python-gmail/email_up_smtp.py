import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587


sender = ''
recipient = '@vtext.com'
passwd = ''

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo
session.login(sender,passwd)

#i ran this on my linux server to let me know if it was up
session.sendmail(sender,recipient,'Linux is up!')
session.quit()
