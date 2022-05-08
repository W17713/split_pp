import os
from imagecls import ObsImage
import pathlib as pl
import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class Splitter:
    def __init__(self,dpath):
        if os.path.exists(pl.Path(dpath)):
            self.rootnode=pl.Path(dpath)
        else:
            self.rootnode=pl.Path(os.getcwd())
        self.classes=os.listdir(self.rootnode)
        self.nclasses=len(self.classes)
    
    def getrootnode(self):
        return self.rootnode

    def getclsitems(self):
        allitems=[None]*len(self.classes)
        for i,j in enumerate(self.classes):
            clsitems=os.listdir(os.path.join(self.rootnode,j))
            allitems[i]=clsitems
        #print(allitems)
        return allitems

    def stageimages(self,imgpath,imgname1,imgname2):
        img=Image.open(os.path.join(imgpath,imgname1))
        img2=Image.open(os.path.join(imgpath,imgname2))
        img=img.convert('L')
        img2=img2.convert('L')
        size1=img.size
        fmt1=img.format
        mode1=img.mode
        size2=img.size
        fmt2=img2.format
        mode2=img2.mode
        #img.imageshow('imgdef')
        #loadedimg=img2.loadimage()
        #print(size1)
        #size2,fmt2,mode2=img2.imageproperties()
        #print(size2)
        #print(fmt1)
        #print(fmt2)
        #print(mode1)
        #print(mode2)
        #img2.imageshow('imgdef')
        if fmt1==fmt2: #= mode2:
            if size1[0]>size2[0]:
                s=size2[0]
            else:
                s=size1[0]
            if size1[1]>size2[1]:
                h=size2[1]
            else:
                h=size1[1]
        #resize images
        shape=(s,h)
        #print(mode1)
        #print(mode2)
        
        a=img.resize(shape)
        b=img2.resize(shape)
        #print(a.size,b.size)
        imagearraya=np.asarray(a)
        imagearrayb=np.asarray(b)
        #print(imagearrayb)
        #print(imagearraya)
        plt.imshow(imagearrayb)
        plt.savefig('imageb.jpeg',cmap='gray')
        return imagearraya,imagearrayb

    def split(self,imagearray,nsplits):
        h=imagearray.shape[0]
        w=imagearray.shape[1]
        x=nsplits/2
        #divide longest side of array(n) into n/2 and other side to 2
        perunit=int(math.floor(nsplits/2)) #floor to prevent odd nsplits
        if h>w:
            otherside=w
            longside=h
        else:
            otherside=h
            longside=w

        dimensions=[] #list of list of tuples to hold portions of
        #divide otherside into 2
        rstart,rend=(0,math.floor(otherside/2))
        rstart2,rend2=(math.floor(otherside/2)+1,otherside-1)

        cstart=cend=-1
        for i in range(perunit):
            cstart=cend+1
            if i==perunit-1:
                #cstart=h-(math.ceil(longside/perunit)*(perunit-1))
                #cstart=cend
                cend=longside-1
            else:
                #cstart=cend+1
                cend=(i+1)*(math.ceil(longside/perunit))
            #each of the two portions of the otherside against n/2 side
            dimensions.append([(rstart,rend),(cstart,cend)])
            dimensions.append([(rstart2,rend2),(cstart,cend)])
        return dimensions
    
    def merge(self,rootnode,cls,imga,imgb,n,b,savepath):#merge in ratio a:b
        imgpath=os.path.join(rootnode,cls)
        imgarra,imgarrb=self.stageimages(imgpath,imga,imgb)
        #imgdima=self.split(imgarra,n)
        imgdimb=self.split(imgarrb,n)
        
        plota=plt.imshow(imgarra,cmap='gray', vmin=0, vmax=255)
        #plt.savefig('imga.jpeg')
        #plt.show()
        plotb=plt.imshow(imgarrb)
        #plt.savefig('imgb.jpeg')
        #plt.show()
        #replace portion of image a array with portion from image b
        for k in range(b):
            x=(n-(k+1))
            rs,re=imgdimb[x][0]
            cs,ce=imgdimb[x][1]
            for i in range(rs,re):#row
                for j in range(cs,ce):#column
                    #print(type(imgarra[i,j]))
                    imgarra[i,j]=imgarrb[i,j].astype(np.uint8)
        plt.imshow(imgarra,cmap='gray', vmin=0, vmax=255) #,
        plt.axis('off')
        #plt.show()
        classpath=os.path.join(savepath,cls)
        plt.savefig(os.path.join(classpath,'i'+imga),bbox_inches='tight',pad_inches = 0)
        
  





        

        
