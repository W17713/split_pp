import os
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import image 
import numpy as np

class ObsImage:
    def __init__(self,ipath,iname):
        self.ipath=ipath
        self.iname=iname

    #load image
    def loadimage(self):
        self.img=Image.open(os.path.join(self.ipath,self.iname))
        return self.img
    def convert(self,b):
        convertedimg=self.img.convert(b)
        return convertedimg

                
    #get image size,type and mode
    def imageproperties(self):
        return self.img.size,self.img.format,self.img.mode
    
    def imagearray(self):
        #imgarray=image.imread(self.img)
        imgarray=np.asarray(self.img)
        return imgarray
    
    def resizeimage(self,size):
        resizedimg=self.img.resize(size,Image.ANTIALIAS)
        return resizedimg

    
    def imageshow(self,type):
        if type=='imgarr':
            arrimg=self.imagearray()
            plt.imshow(arrimg)
        elif type=='imgdef':
            self.img.show()
        else:
            return 'error'
        return 'success'

            






