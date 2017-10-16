#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, unicode_literals

""" Example of browsing for a service (in this case, HTTP) """

import logging
import socket
import sys
from time import sleep
from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf

logging.basicConfig(level=logging.DEBUG)


class BrowseCar():

    def __init__(self):
        self.available_cars = []
        self.zeroconf = None

    def on_service_state_change(self, zeroconf, service_type, name, state_change):
        logging.debug("Service %s of type %s state changed: %s" % (name, service_type, state_change))

        if state_change is ServiceStateChange.Added:
            self.info = zeroconf.get_service_info(service_type, name)
            if self.info:
                data = {};
                data['service_name'] = self.info.name
                data['address'] = socket.inet_ntoa(self.info.address)
                data['port'] = self.info.port

                if self.info.properties:
                    for key, value in self.info.properties.items():
                        data[key] = value
                self.available_cars.append(data)
            else:
                logging.debug("No info in service name: " + name)
        elif state_change is ServiceStateChange.Removed:
            for car in self.available_cars:
                if car['service_name'] == name:
                    self.available_cars.remove(car)
                    break

    def get_available_car(self):
        return self.available_cars

    def start_browser(self, host = "_http._tcp.local."):
        
        self.zeroconf = Zeroconf()
        logging.info("Browsing services")
        browser = ServiceBrowser(self.zeroconf, host, handlers=[self.on_service_state_change])

    def stop_browser(self):
        if self.zeroconf:
            self.zeroconf.close()    
            logging.info("Zerconf browser closed")
        else:

            logging.error("Zeroconf not initiated")


bc = BrowseCar()
try:
    bc.start_browser()
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    bc.stop_browser()
