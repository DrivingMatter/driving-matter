import logging
import socket
import sys
from time import sleep
from zeroconf import ServiceInfo, Zeroconf

logging.basicConfig(level=logging.DEBUG)

class RegisterCar():
    def __init__(self):
        self.zeroconf = None
        self.info = None

    def register_car(self, name):
        my_ip_address = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1] # Link: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib

        if len(my_ip_address) > 0:
            logging.info("Service IP: " + my_ip_address[0])
            my_ip_address = socket.inet_aton(my_ip_address[0])
            
            desc = {'name': name}
            self.info = ServiceInfo("_http._tcp.local.",
                               name + " DrivingMatter._http._tcp.local.",
                               my_ip_address, 80, 0, 0, desc)

            self.zeroconf = Zeroconf()
            logging.info("Registration of a service, press Ctrl-C to exit...")
            self.zeroconf.register_service(self.info)
            return True
        else:
            logging.error("No network interface available, please connect to any network")
            #raise Exception("No network interface")
            return False

    def unregister_car(self):
        if self.zeroconf:
            self.zeroconf.unregister_service(self.info)
            self.zeroconf.close()    
            logging.info("Service unregistered successfully")
        else:
            logging.error("No Zeroconf established yet")

rc = RegisterCar()
try:
    rc.register_car("Mater")
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    rc.unregister_car()
    