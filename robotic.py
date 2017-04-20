'''Kurtis Hall
Object detection
and Sending Email
'''
#!/usr/bin/python

#Importing Libraries: SimpleCV, Emailer, shutil
from SimpleCV import *
import py_gmailer
import shutil

#Starts Camera
cam = Camera()
#Display set to 300 by 300
display = Display((300,300))

#Motion sensitivity using a threshold variable
threshold = 2

#set timer variables for email loop
start_time = time.time()
wait_time = 10 #in seconds

#set a streaming variable to stream webcam online
streaming = JpegStreamer("0.0.0.0:1212")

dirname  = "img"
bkp = "pic_bkp" 
#if the picture directories don't exist, create them



#create a loop that constantly grabs new images from the webcam
while True:
        #set a time variable that updates with the loop
        current_time = time.time()
        #grab an image still from the camera and convert it to grayscale
        img1 = cam.getImage().toGray()
        #wait half a second
        time.sleep(0.5)
	#grab an unedited still to use as our original image
	original = cam.getImage()
        #grab another image still from the camera and conver it to grayscale
        img2 = cam.getImage().toGray()
        #subract the images from each other, binarize and inver the colors
        diff = (img1 - img2).binarize(50).invert()

        #dump all the values into a Numpy matrix and extract the mean avg
        matrix = diff.getNumpy()
        mean = matrix.mean()

	#find and highlight the objects within the image
	blobs = diff.findBlobs()

        #check to see if the wait time has been passed
	if current_time >= (start_time + wait_time):
		#if it has, reset the start time
		start_time = time.time()
		#scan the picture directory for files
		for root, dirs, files in os.walk(dirname):
			dirname_root = root.replace(dirname, bkp)
			#if a file is found in the picture directory, send it to email
			if files:
				firstfile = sorted(files)[0]
				img_mailer = os.path.join(root, firstfile)
				py_gmailer.gmail(img_mailer)
			#move any files in the pic directory to the backup directory
			for file_ in files:
				src_file = os.path.join(root, file_)
				dirname_file = os.path.join(dirname_root, file_)
				shutil.move(src_file, dirname_root)
				
        #if the mean is greater than our threshold variable, then look for objects
	if mean >= threshold:

		#check to see if any objects were detected
		if blobs:
			#find the central point of each object
			#and draw a red circle around it
			for b in blobs:
				try:
					loc = (b.x,b.y) #locates center of object
					img.drawCircle(loc,b.radius(),Color.RED,2)
				except:
					e = sys.exc_info()[0]
		#use the current date to create a unique file name
		timestr = time.strftime("%Y%m%d-%H%M%S")
		
		#initialize the counter variable
		i = 1
		
		#check to see if the filename already exists
		while os.path.exists("pic/motion%s-%s.png" % (timestr, i)):
			#if it does, add one to the filename and try again
			i += 1
		#once a unique filename has been found, save the image
		original.save("pic/motion%s-%s.png" % (timestr, i))
		#print results to terminal
		print("Motion Detected")

	#send the current image to the webcam stream
	original.save(streaming)
