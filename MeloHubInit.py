from tkinter import *;
from seekbar import SeekBar
import time

		
def init(mainframe):
	maincanvas=Canvas(mainframe,bg="black")
	maincanvas.place(x=0,y=0,width=1300,height=700)
	imgfile=PhotoImage(file="icon.png")
	maincanvas.create_image(650,200,image=imgfile)
	maincanvas.create_text((650,300),text="MeloHub",font=("Century Gothic",50,""),justify="center",fill="white")
	maincanvas.create_text((650,370),text="Welcomes You!",font=("Century Gothic",20,""),justify="center",fill="white")
	seekbar=SeekBar(x=50,y=600,height=20,width=1200,parent=maincanvas,activecolour="white",passivecolour="black")
	maincanvas.create_text((95,580),text="Initialising...",font=("Century Gothic",12,""),fill="white")
	

	for x in range(101):
		seekbar.propagate(x)
		mainframe.update()
		time.sleep(0.01)

	maincanvas.destroy()	