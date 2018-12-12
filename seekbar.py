from tkinter import *

class SeekBar():
	def __init__(self,**kwargs):
		self.height=kwargs["height"]
		self.width=kwargs["width"]
		self.activecolour=kwargs["activecolour"]
		self.passivecolour=kwargs["passivecolour"]
		self.c=Canvas(kwargs["parent"],bg="white",bd=0)
		self.c.place(x=kwargs["x"],y=kwargs["y"],height=self.height,width=self.width)
	def propagate(self,percent):
		"""Takes a value in percentage 
		   i.e. from 0 to 100 (both inclusive)"""
		self.c.create_rectangle(0,0,(percent/100)*self.width,self.height,fill=self.activecolour)
		self.c.create_rectangle((percent/100)*self.width,0,self.width,self.height,fill=self.passivecolour)
		
	'''def set(self,event):
		percent=(event.x/self.width)*100
		global csduration
		pygame.mixer.stop()
		pygame.mixer.music.set_pos((percent/100)*csduration*1000)#in milliseconds
		pygame.mixer.music.play()
		self.propagate(percent)'''