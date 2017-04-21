import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def gmail(png_file):
	#add your gmail address and get your stored gmail password from keyring
	gmail_acct = "kurtax.h1@googlemail.com"
	#if you are not using keyring, comment out the text below
	#if you are not using keyring, uncomment the text below
	app_spec_pwd = "kurtax%1"

	#create variables for the "to" and "from" email addresses
	TO = ["kurtax.h1@googlemail.com"]
	FROM = "kurtax.h1@googlemail.com"

	#asemble the message as "MIMEMultipart" mixed
	msg = MIMEMultipart('mixed')
	msg['Subject'] = 'Important Message!'
	msg['From'] = FROM
	msg['To'] = ', '.join(TO)
	body = MIMEText('Intruder has been loacated!', 'plain')
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
