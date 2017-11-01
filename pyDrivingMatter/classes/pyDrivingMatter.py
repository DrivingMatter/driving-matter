import websocket
import io
import cv2
import numpy as np
from PIL import Image
from time import time, sleep
import logging
from threading import Thread

from .KBhit import KBHit
from .BrowseCar import BrowseCar

class pyDrivingMatter():
    bc = None
    def __init__(self):
        self.bc = BrowseCar()
        self.bc.start_browser()

    def available_cars(self):
        return self.bc.get_available_car()

    # Destructor
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.bc.stop_browser()