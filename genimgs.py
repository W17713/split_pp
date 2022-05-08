import os
from splittercls import Splitter 


path='/home/ababelrmah/nn_ppml/PriMIA/data/oldtrain'
savepath='/home/ababelrmah/nn_ppml/PriMIA/data/train'

spl=Splitter(path)

def start(n,b):
	rootnode=spl.getrootnode()
	classes=os.listdir(rootnode)
	for i,j in enumerate(classes):
		imgs=os.listdir(os.path.join(path,j))
		for k,img in enumerate(imgs):
			if k < len(imgs)-1:
				#print(imgs[k+1])
				#print(str(rootnode)+' '+str(j)+' '+str(img))
				spl.merge(rootnode,j,img,imgs[k+1],n,b,savepath)
				spl.merge(rootnode,j,imgs[k+1],img,n,b,savepath)

if __name__=="__main__":
	options=[4,8]
	sizopts=[1,3]
	for a in options:
		for b in sizopts:
			start(a,b)
	
