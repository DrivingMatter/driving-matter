import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import cv2
import numpy as np
import math
import threading
from threading import Thread
from multiprocessing import Process,Pool
from functools import partial
#current frame rate -> 4-5 fps with 98.03 % accuracy and 0.3 FalseAlarm


class SignDetection:

    def __init__(self):
        self.image=[]
        self.sign={}
         
        self.sign['Traffic light']= cv2.CascadeClassifier("classifiers/16/cascade.xml")
        self.sign['Stop']= cv2.CascadeClassifier("classifiers/HAAR/stopsign_classifier.xml")
        self.sign['No Left'] = cv2.CascadeClassifier("classifiers/HAAR/noleftturn_classifier.xml")
                
        self.detected = {
		"Stop" : False,
		"No Left" : False,
		"Red Light" : False,
		"Green Light" : False,
		"Yellow Light" : False		
	    }
        self.alpha = 8.0 * math.pi / 180
        self.v0 = 119.865631204
        self.ay = 332.262498472
        self.focal_length=(57*40)/4.5
        
    def destroy(self):
        self.detected = {
		"Stop" : False,
		"No Left" : False,
		"Red Light" : False,
		"Green Light" : False,
		"Yellow Light" : False		
	    }
        self.image=[]
        
        
    def worker(arg):
        classifier, image, type = arg
        return self.detect_obj(classifier,image, type)

    def detect_obj(self,classifier,image,type=""):
        self.image=image
        
        v=0
        #self.image = cv2.pyrDown(self.image)
        
        #self.image=cv2.resize(self.image,(int(width/10),int(height/10)),interpolation=cv2.INTER_AREA)
        gray_image = cv2.cvtColor(self.image , cv2.COLOR_BGR2GRAY)
        if type=='Traffic light':
            sign=classifier.detectMultiScale(
            gray_image,
            scaleFactor=1.02,
            minNeighbors=2,
            minSize=(40,40),
            flags=cv2.CASCADE_SCALE_IMAGE
            )
        else:    
            sign=classifier.detectMultiScale(
                gray_image,
                scaleFactor=1.2,
                minNeighbors=2,
                minSize=(20,20),
                flags=cv2.CASCADE_SCALE_IMAGE
                )
        
        for (x,y,w,h) in sign:
            cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,219,0),2)
            v = y + h - 5
           # d=self.distance_to_camera(v, 15.5 - 10, 300)
            d=self.distance_to_camera_temp(v)
            cv2.putText(self.image, "%s %.1fcm" %(type, d), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,219,0), 1)
     	    self.detected[type]=True
            if type=='Traffic light':
                boundaries = [
                  ([17, 15, 100], [50, 50, 204]),  #red
                #	([255, 178, 189], [229, 25, 54]),      #green
                  ([100, 25, 6], [255, 178, 233]),  #green is yet to find
                  ([25, 146, 190], [62, 174, 250])] 
                roi=self.image[y+5:y + h-5, x+15:x + w-15] 
                roi = cv2.blur(roi,(5,5))
    
                for (lower, upper) in boundaries:
                    lower = np.array(lower, dtype = "uint8")
                    upper = np.array(upper, dtype = "uint8")
                    
                   
                    gray = cv2.cvtColor(cv2.bitwise_and(roi, roi, mask = cv2.inRange(roi, lower, upper)) , cv2.COLOR_BGR2GRAY)        
                    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
                    pos=len(gray)/3
                    if maxVal:
                        if pos > maxLoc[1]:
                            #cv2.putText(self.image, 'Red', (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                            self.detected['Red Light'] = True
                            break
                        
                        # Green light  (This has problem, becuase of range)
                        elif 3*pos > maxLoc[1] > 2*pos:
                            #cv2.putText(self.image, 'Green', (x+5, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                            self.detected['Green Light'] = True
                            break
                        # yellow light
                        elif 2*pos > maxLoc[1] > pos:
                            #cv2.putText(self.image, 'Yellow', (x+5, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
                            self.detected['Yellow Light'] = True
                            break
                    
                
    
        
    def detect(self,image):
        self.image=image
            
        signs = [key for key in self.sign]
##       pool = Pool(3)
##        pool.map(self.worker, ((self.sign[key], image, key) for key in self.sign))
##        pool.close()
##        pool.join()
##        for type in signs:
##            self.detect_obj(self.sign[type],image,type)
##        
        t={}
        for type in signs:
            t[type]=Thread(target = self.detect_obj,args=(self.sign[type],self.image,type))
            t[type].start()
##            t[type].join()
        [t[type].join() for type in signs]    
        detected={}    
        image=self.image
        detected=self.detected
        self.destroy()
        return detected,image
    
    def distance_to_camera(self, v, h, x_shift):
        return h / math.tan(self.alpha + math.atan((v - self.v0) / self.ay))
    
    def distance_to_camera_temp(self,v):
        return (4.5*self.focal_length)/v
       
