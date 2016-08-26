import os
import ImageGrab
import pymouse


def screenShot(coords=[0,0,1,1]):
	print "picing"
	img = ImageGrab.grab(bbox = coords)
	img.save(folderName+"/"+"yo.jpg")
	

def makeFolder(pathName):#param is folder name
	if not os.path.exists(pathName):
		os.mkdir(pathName)



if __name__ == "__main__":
	folderName = "container"
	makeFolder(folderName)

	screenShot()
