from time import sleep
import logging

from .BrowseCar import BrowseCar

logger = logging.getLogger(__name__)

class pyDrivingMatter():
    bc = None
    def __init__(self):
        self.bc = BrowseCar()
        self.bc.start_browser()

    def available_cars(self):
        return self.bc.get_available_car()

    def get_car(self):
        cars = []
        while True:
            cars = pydm.available_cars()
            if len(cars) == 0:
                logger.debug("Waiting for cars on network")
            else: 
                break
            sleep(1)

        car_data = cars[0]

        if len(sys.argv) == 2 and sys.argv[1] == "find_my_car":
            logging.debug ("="*80)
            logging.debug (car_data)
            logging.debug ("="*80)
            sys.exit()

        car_link = "ws://{}:{}".format(car_data['address'], car_data['port'])
        return car_data, car_link

    # Destructor
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.bc.stop_browser()