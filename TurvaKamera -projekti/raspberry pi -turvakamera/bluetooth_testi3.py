import bluetooth
target_name= 'Honor Play JE'
target_address = None
nearby_devices=bluetooth.discover_devices()
print(nearby_devices)
for bdaddr in nearby_devices:
    if target_name == bluetooth.lookup_name( bdaddr ):
        target_address = bdaddr
        print("ok")
        break
