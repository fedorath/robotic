import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) #Right IR sensor module
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Activation button
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Left IR sensor module

GPIO.setup(26,GPIO.OUT) #Left motor control
GPIO.setup(24,GPIO.OUT) #Left motor control
GPIO.setup(19,GPIO.OUT) #Right motor control
GPIO.setup(21,GPIO.OUT) #Right motor control

pwm = PWM(0x40, debug = False)
        pwm.setPWMFreq(60)
 #use pwm on inputs so motors don't go too fast
GPIO.setup(26, GPIO.OUT)
p = GPIO.PWM(26, 20)
p.start(0)

GPIO.setup(24, GPIO.OUT)
q = GPIO.PWM(24, 20)
q.start(0)

GPIO.setup(19, GPIO.OUT)
a = GPIO.PWM(19, 20)
a.start(0)

GPIO.setup(21, GPIO.OUT)
b = GPIO.PWM(21, 20)
b.start(0)


#Motor stop/brake
GPIO.output(26,0) 
GPIO.output(24,0)
GPIO.output(19,0)
GPIO.output(21,0)
speed = 50
flag=0
while True:
	j=GPIO.input(13)
	if j==1: #Robot is activated when button is pressed
		flag=1
		print "Robot Activated",j
	
	while flag==1:
		i=GPIO.input(7) #Listening for output from right IR sensor
		k=GPIO.input(11) #Listening for output from left IR sensor
		if i==0: #Obstacle detected on right IR sensor
			print "Obstacle detected on Right",i 
			#Move in reverse direction
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

			#Turn robot left
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(speed)
    			b.ChangeDutyCycle(0)
    			q.ChangeFrequency(speed + 5)
    			a.ChangeFrequency(speed + 5)
		if k==0: #Obstacle detected on left IR sensor
			print "Obstacle detected on Left",k
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)
			
    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			p.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

		elif i==0 and k==0:
			print "Obstacles on both sides"
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(speed)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			q.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)

    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(speed)
    			p.ChangeFrequency(speed + 5)
    			b.ChangeFrequency(speed + 5)
			
		elif i==1 and k==1:	#No obstacles, robot moves forward
			print "No obstacles",i
			#Robot moves forward
    			p.ChangeDutyCycle(speed)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(speed)
    			b.ChangeDutyCycle(0)
   			p.ChangeFrequency(speed + 5)
    			a.ChangeFrequency(speed + 5)
		j=GPIO.input(13)
		if j==1: #De activate robot on pushin the button
			flag=0
			print "Robot De-Activated",j
    			p.ChangeDutyCycle(0)
    			q.ChangeDutyCycle(0)
    			a.ChangeDutyCycle(0)
    			b.ChangeDutyCycle(0)
