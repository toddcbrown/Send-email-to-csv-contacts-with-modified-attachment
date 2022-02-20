
# install yagmail
import yagmail
import os 
import time 
import pandas
df = pandas.read_csv('contacts.csv')

my_secret = os.environ['PASSWORD']
sender = 'boor3657@gmail.com'
attachment = 'bill.txt'
subject = 'Sutro Jersey '
contents = ''

for i in df.index:
  yag = yagmail.SMTP(user=sender,password=my_secret)
  contents = 'Hi %s! You owe $%s pay now please!\nThanks!\nTodd\n----'%(df.name[i],df.amount[i])
  attach = df.filepath[i]#str('attachments/%s'%df.filepath[i])
  yag.send(df.email[i],subject=subject,contents=contents,attachments=attach)
  print(df.name[i], ' email sent')
  
