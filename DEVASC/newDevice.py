import Devices

rtr1 = Devices.Router('Cisco ISR 4080', 'IOS 14.5.1', '10.10.250.250')
sw1 = Devices.Switch('Cisco Catalyst 3850', 'IOS 10.5.4', '10.10.250.251')

print(f'Router 1\n{rtr1.getdesc()}\n', sep='')
print(f'Switch 1\n{sw1.getdesc()}',sep='')