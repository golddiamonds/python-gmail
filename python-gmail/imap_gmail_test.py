import imaplib
import os
from pprint import pprint
import smtplib
import time

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

#user gmail username for sender
sender = ''
#I have verizon. e.g. 1234567890@vtext.com
recipient = '@vtext.com'
#enter gmail password here
passwd = ''

unseen_msgs = 0
on = 1
while (on == 1):
    connection = imaplib.IMAP4_SSL('imap.gmail.com')
    username = (sender)
    password = (passwd)
    connection.login(username,password)
    prev_unseen_msgs = int(unseen_msgs)
    typ, data = connection.select('INBOX')
    print 'Response code:', typ
    print 'Response: '
    pprint(data)
    num_msgs = int(data[0])
    print num_msgs
    print connection.status('INBOX', '(MESSAGES RECENT UIDNEXT UIDVALIDITY UNSEEN)')
    data2 = connection.status('INBOX', '(UNSEEN)')
    print data2[1][0]
    unseen1 = data2[1][0]
    unseen2 = unseen1[16:]
    print unseen1
    print unseen2
    unseen3 = unseen2[:-1]
    print unseen3
    unseen_msgs = int(unseen3)
    if (int(unseen3) > 0) & (prev_unseen_msgs != unseen_msgs):
        print 'New Mail!'

        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(sender,passwd)

        session.sendmail(sender,recipient,'You have ' + unseen3 + ' message!')
        session.quit()
    else:
        print 'No new mail :('
    connection.logout()
    time.sleep(300)
