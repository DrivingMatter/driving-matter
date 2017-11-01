import os
import numpy as np
from PIL import Image
import pandas
import cv2
import time
import datetime
import csv
class Dataset:
    directory = None
    filename = None

    
    def __init__(self, directory, filename):
        self.directory=directory
        self.filename=filename
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.exists(self.directory+'/'+self.filename):
            with open(self.directory+'/'+self.filename,'wb') as newFile:
                newFileWriter = csv.writer(newFile)
                newFileWriter.writerow(['time','dist1','dist2', 'dist3','camR','camC','camL','action','ack'])
   
    def save_data(self,image) :
        imagedirectory=self.directory+'/images'
        ctime=time.time()
        image_name = str(ctime)+ ".jpg"
        #print(image_name)
        if not os.path.exists(imagedirectory):
            os.makedirs(imagedirectory)
        cv2.imwrite(os.path.join(imagedirectory, image_name), image)
        
        dist1=1
        dist2=2
        dist3=3
        Dict = {'time': ctime, 'dist1': dist1, 'dist2': dist2, 'dist3': dist3, 'camR': 'NaN', 'camC': imagedirectory+'/'+image_name , 'camL':'NaN', 'action': 'D', 'ack': 'D',}
        self.add_data(Dict)

    
    def add_data(self,data):
       with open(self.directory+'/'+self.filename, 'rb') as newFile:
           header = next(csv.reader(newFile))
       with open(self.directory+'/'+self.filename, 'ab') as newFile:   
           dict_writer = csv.DictWriter(newFile, header, -999)
           dict_writer.writerow(data)

    def get_dataset(self):
        data = pandas.read_csv(self.filename)
        return data
