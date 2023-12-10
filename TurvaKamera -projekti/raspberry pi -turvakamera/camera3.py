import cv2
import time
from datetime import datetime
from PIL import Image
import RPi.GPIO as GPIO
import bluetooth

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

camera = cv2.VideoCapture(0)

def TurvaKamera():
	for i in range(2):
		date= datetime.fromtimestamp(time.time())
		return_value, image = camera.read()
		cv2.imwrite("/home/pi/Kuvat/"+str(date)+".jpg", image)
	date= datetime.fromtimestamp(time.time())
	f=open("/home/pi/Asiakirjat/TurvaKamera/"+str(date)+".txt","w")
	f.write(str(date)+(".jpg	Ääni tunnistettu. Kuva otettu!"))
	f.close
	print(date)
def main():
	target_name= 'Honor Play JE'
	target_address = None

	while True:
		nearby_devices=bluetooth.discover_devices()
		for bdaddr in nearby_devices:
			if target_name == bluetooth.lookup_name( bdaddr ):
				target_address = bdaddr
				break
		if target_address is not None:
			print("Puhelin tunnistettu. Sammutetaan turvakamera.")
			break
		elif GPIO.input(channel):
			print("Sound Detected!")
			TurvaKamera()
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, main)  # assign function to GPIO PIN, Run function on change
if __name__=='__main__':
	main()

