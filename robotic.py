'''Kurtis Hall
Object detection
and Sending Email
'''
#!/usr/bin/python

#Importing Libraries: SimpleCV, Emailer, shutil
from SimpleCV import *
import time
import py_gmailer
import shutil
#initialize the counter variable
i = 1	

#Starts Camera
cam = Camera()
disp = Display(cam.getImage().size())
#Motion sensitivity using a threshold variable
threshold = 1

#set timer variables for email loop
start_time = time.time()
wait_time = 30 #in seconds

dst = "Kurt"
bkp = "pic_bkp" 
#if the picture directories don't exist, create them
if not os.path.exists("Kurt"):
	os.makedirs("Kurt")
if not os.path.exists("pic_bkp"):
	os.makedirs("pic_bkp")

#create a loop that constantly grabs new images from the webcam
while True:
        current_time = time.time()
	
        img01 = cam.getImage().toGray()
	time.sleep(1)
	#grab an unedited still to use as our original image
        OIMG = cam.getImage()
	img02 = cam.getImage().toGray()

	
	diff = (img01 - img02).binarize(50).invert()
	
        matrix = diff.getNumpy()
        mean = matrix.mean()

	#find and highlight the objects within the image
	faces = diff.findHaarFeatures('face')

        #check to see if the wait time has been passed
	if current_time >= (start_time + wait_time):
		#if it has, reset the start time
		start_time = time.time()
		#scan the picture directory for files
		for root, dirs, files in os.walk(dst):
			dst_root = root.replace(dst, bkp)
			#if a file is found in the picture directory, send it to email
			if files:
				firstfile = sorted(files)[0]
				img_mailer = os.path.join(root, firstfile)
				py_gmailer.gmail(img_mailer)
			#move any files in the pic directory to the backup directory
			for file_ in files:
				src_file = os.path.join(root, file_)
				dst_file = os.path.join(dst_root, file_)
				shutil.move(src_file, dst_root)
				
        #if the mean is greater than our threshold variable, then look for objects
	if mean >= threshold:

		#check to see if any objects were detected
		if faces is not None:
			faces = faces.sortArea()
			bigFace = faces[-1]

			bigface.draw()
		#use the current date to create a unique file name
		timestr = time.strftime("%y%a%H%M")	
		
		while os.path.exists("pic/motion%s-%s.png" % (timestr, i)):
			#if it does, add one to the filename and try again
			i += 1
		
		
		OIMG.save("Kurt/INTRUDER%s-%s.png" % (timestr, i))
		#Terminal prints "detected intruder"
		print("Detected intruder!")
		
	
