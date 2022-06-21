import smtplib
from email.mime.text import MIMEText

from_acc = 'your mail'
to_acc = 'send to mail'
pwd = input('請輸入密碼: ')

# for chinese
msg = 'message'

mailset =  MIMEText(msg, 'plain', 'utf-8')
mailset['Subject'] = '主旨'
mailset['From'] = '寄件人名稱'
mailset['To'] = '收件人名稱'

# for english
# msg = 'Subject: This is subnect\n'\
#     'From: from user\n'\
#     'To: to others\n'\
#     'Message is here. Try it.'


mysmtp = smtplib.SMTP('smtp.gmail.com', 587)
mysmtp.ehlo()
mysmtp.starttls()
mysmtp.login(from_acc, pwd)
status = mysmtp.sendmail(from_acc, to_acc, mailset.as_string())
if status == {}:
    print('Send mail success')
mysmtp.quit()
