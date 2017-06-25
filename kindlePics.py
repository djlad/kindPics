import os
from PIL import ImageGrab
import pymouse
import pykeyboard
import time
import shutil

def screenShot(coords=[0,0,1,1],name="yo.jpg"):
	print "taking picture"
	img = ImageGrab.grab(bbox = coords)
	img.save(folderName+"/"+name)
	

def makeFolder(pathName):#param is folder name
	if not os.path.exists(pathName):
		os.mkdir(pathName)

class boxListener(pymouse.PyMouseEvent):
	def __init__(self, pages):
		self.picBox = [0,0,0,0]
		self.firstClick = True
		self.kb = pykeyboard.PyKeyboard()
		self.pages = pages
		pymouse.PyMouseEvent.__init__(self)
	
	def takeScreenShots(self, pages):
		for i in range(self.pages):
			print self.picBox
			screenShot(self.picBox,str(i)+".jpg")
			self.kb.tap_key(self.kb.right_key)
			time.sleep(.1)
		self.stop()

	def click(self,x,y,button,press):
		if press:
			if self.firstClick:
				self.picBox[0] = x
				self.picBox[1] = y
				self.firstClick = False
				print "click bottom right corner of page."
			else:
				self.picBox[2] = x
				self.picBox[3] = y
				self.takeScreenShots(pages)


	

if __name__ == "__main__":
	folderName = "kindlepicscontainer"
	makeFolder(folderName)

	pages = raw_input("enter number of pages: ")
	pages = int(pages)
	a = boxListener(pages)
	print "click top left corner of page"
	a.run()
	print "this is a thread"
