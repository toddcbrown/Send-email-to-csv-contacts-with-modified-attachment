# install yagmail
import yagmail
import os 
sender = 'boor3657@gmail.com'
receiver = 'xirix46505@sueshaw.com'
subject = 'This be the subject'
contents = """
These are the contents of the email
"""

my_secret = os.environ['PASSWORD']

yag = yagmail.SMTP(user=sender,password=my_secret)
yag.send(to=receiver,subject=subject,contents=contents)
print('Email Sent!') 

"""count = 3
while count > 0:
  yag.send(to=receiver,subject=(str(count ) + subject),contents=(st(count) + contents))
  print('Email %s sent'%count)
  count -= 1 
"""
