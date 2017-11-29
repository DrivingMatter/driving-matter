import os
import numpy as np
from PIL import Image
import pandas
import cv2
import time
import datetime
import csv

class Dataset:
    def __init__(self, base = "dataset/", filename = "dataset.csv"):
        self.base = os.getcwd() + "/" + base
        self.directory = self.base + str(time.time()) + "/"
        self.csv_file_path = self.directory + filename
        self.images_path = self.directory + "images/"

        if not os.path.exists(self.images_path):
            os.makedirs(self.images_path)

        if not os.path.exists(self.csv_file_path):
            with open(self.csv_file_path, 'wb') as newFile:
                # file created.
                pass
                
        self.csv_file_writer = open(self.csv_file_path, 'ab')
        self.header = None

    def save_data(self, datavector, dataset_title):
        if self.header is None:
            self.header = dataset_title
            csv_writer = csv.writer(self.csv_file_writer)
            csv_writer.writerow(self.header)

        image_name = str(time.time())+ ".jpg"
        
        for key in datavector:
            value = datavector[key]
            # save images
            if "camera" in key:
                name = key + "_" + image_name
                path = self.images_path + name
                value.save(path)        
                datavector[key] = path

        self.add_data(datavector)
    
    def add_data(self, data):
       dict_writer = csv.DictWriter(self.csv_file_writer, self.header, -999)
       dict_writer.writerow(data)
       self.csv_file_writer.flush()

    def get_dataset(self):
        data = pandas.read_csv(self.csv_file_path)
        return data
