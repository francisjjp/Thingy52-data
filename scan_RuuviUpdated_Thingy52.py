from bluepy.btle import *
import re


def scan():
        scanner = Scanner(0)
        devices = scanner.scan(3) # List of ScanEntry objects
        while True:
            scanner = Scanner(0)
            devices = scanner.scan(3)  # List of ScanEntry objects
            for dev in devices:
                for (adtype, desc, value) in dev.getScanData():
                    if re.search('Ruuvi.+',value) or 'Thingy' in value:
                        print("addr {}, addrtype {}, value {}".format(dev.addr, dev.addrType, value))

scan()
