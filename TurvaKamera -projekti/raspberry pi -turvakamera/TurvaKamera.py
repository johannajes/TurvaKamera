import cv2
import time
from datetime import datetime
from PIL import Image
import RPi.GPIO as GPIO
#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

camera = cv2.VideoCapture(0)

def TurvaKamera():
	
	for i in range(2):
		return_value, image = camera.read()
		cv2.imwrite("/home/pi/Kuvat/img"+str(i)+".jpg", image)
		
		#kuva=Image.open("/home/pi/Kuvat/img"+str(i)+".jpg")
		date= datetime.fromtimestamp(time.time())
		f=open("/home/pi/Asiakirjat/TurvaKamera/"+str(date)+".txt","w")
		f.write(str(date)+"img"+str(i)+(".jpg	Kuva otettu!"))
		f.close
		time.sleep(2)
	print(date)
def main():
	while True:
		if GPIO.input(channel):
			print("Sound Detected!")
			TurvaKamera()
		#else:
			#print("Sound Detected!")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, main)  # assign function to GPIO PIN, Run function on change
if __name__=='__main__':
	main()
