#import the SimpleCV library
from SimpleCV import *

#initialize the camera
cam = Camera()

#grab the image from the camera
img  = cam.getImage()
#show the image in a new window
img.show()
#save the image to a file within the project folder
img.save('image.png')
