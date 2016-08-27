import os
import ImageGrab
import pymouse
import pykeyboard
import time

def screenShot(coords=[0,0,1,1],name="yo.jpg"):
	print "picing"
	img = ImageGrab.grab(bbox = coords)
	img.save(folderName+"/"+name)
	

def makeFolder(pathName):#param is folder name
	if not os.path.exists(pathName):
		os.mkdir(pathName)


class boxListener(pymouse.PyMouseEvent):
	def __init__(self):
		self.picBox = [0,0,0,0]
		self.firstClick = True
		self.kb = pykeyboard.PyKeyboard()
		pymouse.PyMouseEvent.__init__(self)
	
	def takeScreenShots(self):
		for i in range(20):
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
			else:
				self.picBox[2] = x
				self.picBox[3] = y
				self.takeScreenShots()


	

if __name__ == "__main__":
	folderName = "container"
	makeFolder(folderName)

	screenShot()
	a = boxListener()
	a.run()
	print "this is a thread"
