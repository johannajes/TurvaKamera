
from bluetooth import *

print ("performing inquiry...")

nearby_devices = discover_devices(lookup_names = True)

print ("found %d devices" % len(nearby_devices))

for name, addr in nearby_devices:
     print (" %s - %s" % (addr, name))
     
'''mport bluetooth

nearby_devices = bluetooth.discover_devices()
print (nearby_devices)'''
if "34:12:F9:E9:49:0A" in nearby_devices:
	print("True")
else:
	print("False")
