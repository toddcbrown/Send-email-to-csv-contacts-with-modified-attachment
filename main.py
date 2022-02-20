
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

yag = yagmail.SMTP(user=sender,password=my_secret)

def generate_file(filename,content):
  with open(filename, 'w') as file:
    file.write(str(content))

for index,row in df.iterrows():
  name = row['name']
  filename = name + '.txt'
  amount = row['amount']

  generate_file(filename,amount)

  receiver_email = row['email']
  subject = 'This is your final notice!'
  contents = [f""" 
  Hey, {name} you have to pay {amount}.
  Bill is attached, you butthole.
  """,filename,
  ]

  yag.send(to=receiver_email,subject=subject,contents=contents)
  
