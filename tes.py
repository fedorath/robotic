##########################################################################################################
##########################################################################################################
###################################   Kurtis Hall 14019369 Project   #####################################
##########################################################################################################
##########################################################################################################

#Multiple imports
import os
import time
from SimpleCV import *
import smtplib
from datetime import datetime as dt
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##########################################################################################################
#				Sending Attached PNG files to recipient.			         #
##########################################################################################################

def email(Gmail):

	img_data = open(Gmail, 'rb').read()
        msg = MIMEMultipart('mixed')
        msg['Subject'] = 'Important Message!'#subject title
        msg['From'] = 'kurtax.h1@googlemail.com'
        msg['Reply-to'] = ', '.join('kurtax.h1@googlemail.com')
        text = MIMEText("Intruder has been spotted!")#email body text
        msg.attach(text)#attach body text
        image = MIMEImage(img_data, name=os.path.basename(Gmail))
        msg.attach(image)#attaches img

        s = smtplib.SMTP('smtp.gmail.com', 587)#SMTP server connection
        s.ehlo()
        s.starttls()#Starts transport layer security
        s.ehlo#Extended hello command
        s.login('kurtax.h1@googlemail.com', 'kurtax%1')#Login Details
        s.sendmail('kurtax.h1@googlemail.com','kurtax.h1@googlemail.com', msg.as_string())#Sending email
        s.close()#Closes
	
##########################################################################################################
#					SimpleCV Object detection.				         #
##########################################################################################################
fmt = "%Y-%m-%d %H-%M-%S"#Date,Month,Year,Hour,Minute,Seconds
IMG = Camera()#Camera is intiated.
width = 640
height = 480
directory = "Photo" #Directory name photo
if not os.path.exists("Photo"):#checks if exists
	os.makedirs("Photo")#makes directory
Time = 10#Time it takes to send the email
sleep = 0.2
Stime = time.time()
	
while True:#While loop which grabs images until it is told to stop.
	settime = time.time()	
        PIC1 = IMG.getImage().toGray()
	time.sleep(sleep)
	PIC = IMG.getImage()
        PIC2 = IMG.getImage().toGray()
        d = (PIC1 - PIC2).binarize().invert()
        matrix = d.getNumpy()
        avg = matrix.mean()
	radius = d.findBlobs()
##########################################{Blob}##########################################				
	
	
	if avg >= 10: #average mean greater equal to 10
		if blobs:

			for blob in blobs:
				try: #Draws green circles around the detected objects
					blob = radius
					PIC.drawCircle((blob.x,blob.y),blob,SimpleCV.Color.GREEN,3)
				except:
					e = sys.exc_info()[0]
					
					
###################################{Names and saves image}###################################################


		name = dt.now().strftime(fmt) # filename is set using date and time
		i = 1
		while os.path.exists("Photo/Intruder%s-%s.png" % (name, i)):
			i += 1
		PIC.save("Photo/Intruder%s-%s.png" % (name, i))#saves photo with name
		
		
		#prints them into terminal
		print("Initiating Camera!")
		print ("Processing %s...") 
		print ("Intruder Image Stored!")
		

	if settime >= (Stime + Time):
		for root, dirs, files in os.walk(directory, topdown=False):#checks the folder for images
			for file in files:#finds the image
				Sortfile = sorted(files)[0]
				mailer = os.path.join(root, Sortfile)
				email(mailer)#sends image to email function
				
				

##########################################################################################################
#						The END!					         #
##########################################################################################################
