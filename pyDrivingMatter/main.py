from pyDrivingMatter import pyDrivingMatter
from KBhit import KBHit

with pyDrivingMatter() as pydm:
    cars = pydm.available_cars()

    if len(cars) == 0:
        raise EnvironmentError("No car available")

car_data = cars[0]

car_link = "{}:{}".format(car_data['address'], car_data['port'])
action_link = "{}/action"
camera_c_link = "{}/camera_c"

car = Car(action_link, camera_c_link)

def handle_camera_c(data):
    stream = io.BytesIO()
    stream.write(data)
    stream.seek(0)
    img = np.asarray(Image.open(stream))
    cv2.imshow("camera_c", img)
    stream.seek(0)
    key = cv2.waitKey(1) & 0xFF

car.set_camera_c_callback(handle_camera_c)

try:
    kb = KBHit()
    while True:
        if kb.kbhit():
            c = kb.carkey()
            if c == 0: # Up
                car.forward()            
            elif c == 1: # Right
                car.right() 
            elif c == 2: # Down
                car.backward()              
            elif c == 3: # Left
                car.left()              
            elif c == 4: # Space
                car.left()              


finally:
    kb.set_normal_term()    
    cv2.destroyWindow("camera_c")