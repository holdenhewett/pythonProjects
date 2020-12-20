import Devices

rtr1 = Devices.Router('Cisco ISR 4080', 'IOS 14.5.1', '10.10.250.250')

print('Router1\n', rtr1.getdesc(), '\n', sep='')