import cv2						# Tarvitaan kameran yhdistamiseen
import time
from datetime import datetime
from PIL import Image			# Kuvanmuokkausta varten
import RPi.GPIO as GPIO			# Tunnistaa Raspin pinnit
import bluetooth

#GPIO SETUP
channel = 17					# Raspin pin, johon piirilevy yhditetty
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

camera = cv2.VideoCapture(0)

def TurvaKamera():
	for i in range(10):					# Kamera ottaa kuvasarjan
		date= datetime.fromtimestamp(time.time())
		return_value, image = camera.read()
		cv2.imwrite("/home/pi/Kuvat/"+str(date)+".jpg", image)
	date= datetime.fromtimestamp(time.time())
	f=open("/home/pi/Asiakirjat/TurvaKamera/"+str(date)+".txt","w")
	f.write(str(date)+(".jpg	Ääni tunnistettu. Kuva otettu!"))	#tiedosto nimetään ajan mukaan, jottei se kirjoita edellisten tiedostojen päälle
	f.close								# Lisätään tiedostoon, koska kuvia on otettu
	print(date)
def main():
	target_name= 'Honor Play JE'
	target_address = None
	while True:
		nearby_devices=bluetooth.discover_devices()	
		for bdaddr in nearby_devices:			# Tarkistetaan, onko omistaja kotona
			if target_name == bluetooth.lookup_name( bdaddr ):
				target_address = bdaddr
				break
		if target_address is not None:
			print("Puhelin tunnistettu. Sammutetaan turvakamera.")
			break
		elif GPIO.input(channel):			# Kuuntelee ääntä
			print("Sound Detected!")
			TurvaKamera()				# Käynnistää turvakameran funktio kutsulla
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  	# Kertoo onko pin HIGH vai LOW
GPIO.add_event_callback(channel, main)  			# asetetaan functio GPIO PIN:lle, ajaa function sen muuttuessa
if __name__=='__main__':
	main()

