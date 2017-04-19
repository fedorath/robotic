'''PYTHON GMAILER
This code is intended to send 
messages with attachments 
through gmail using python.
________________________________
How to get this code working
________________________________
INSTALL KEYRING
-pip install keyring
INSTALL KEYRING ALT
wget https://pypi.python.org/packages/source/k/keyrings.alt/keyrings.alt-1.1.tar.gz
tar -zxvf keyrings.alt-1.1.tar.gz
cd keyrings.alt-1.1
python setpy.py install
STORE YOUR CREDENTIALS IN KEYRING
keyring --help
keyring set [section ex.email] [username]
	[enter in your password]
keyring get [section to retrieve] [username to retrieve]
ENABLE GMAIL TO ALLOW THIRD-PARTY PROGRAMS
- without dual authentication: http://www.google.com/settings/security/lesssecureapps
- without dual authentication: https://security.google.com/settings/security/apppasswords
'''

#import the SMTP and Keyring libraries
import smtplib
#if you are not using keyring, comment out the text below
import keyring

#import the Text,Image and Multipart modules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def gmail(png_file):
	#add your gmail address and get your stored gmail password from keyring
	gmail_acct = "kurtax.h1@googlemail.com"
	#if you are not using keyring, comment out the text below
	app_spec_pwd = keyring.get_password("credentials", "gmail")
	#if you are not using keyring, uncomment the text below
	app_spec_pwd = "kurtax%1"

	#create variables for the "to" and "from" email addresses
	TO = ["kurtax.h1@googlemail.com"]
	FROM = "kurtax.h1@googlemail.com"

	#asemble the message as "MIMEMultipart" mixed
	msg = MIMEMultipart('mixed')
	msg['Subject'] = 'Intruder Alert!'
	msg['From'] = FROM
	msg['To'] = ', '.join(TO)
	body = MIMEText('Motion was detected on your security camera.', 'plain')
	msg.attach(body)

	#open up an image file and attach it to the message
	img_data = open(png_file, 'rb')
	image = MIMEImage(img_data.read())
	img_data.close()
	msg.attach(image)

	#open up the SMTP server, start a tls connection, login, send, and close
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo
	server.login(gmail_acct, app_spec_pwd)
	server.sendmail(FROM, TO, msg.as_string())
	server.close()
