from SimpleCV import Image, Camera, Display
import sys


disp = Display((640,480))

def tryit(i):
    try:
        if i>=5:
            print "Nao Existe Camera!"
            sys.exit()

        cam = Camera(i)
        while disp.isNotDone():
            img = cam.getImage()
            img.save(disp)
    except:
        i+=1
        tryit(i)

tryit(-1)
