from tkinter import *
from seekbar import SeekBar
import os 
import pygame
import mutagen.mp3
import threading
import MeloHubInit

root = Tk()
root.geometry("1300x700")
root.title("MeloHub")
MeloHubInit.init(root)

#colours used
backgroundcolor="#005ac0"
selectbackgroundcolour="#00ffaa"
foregroundcolour="white"
selectforegroundcolour="black"

#images used
playimage=PhotoImage(file="C:\\Users\\Karan12\\Documents\\PythonProjects\\MusicPlayer\\play.png")
pauseimage=PhotoImage(file="C:\\Users\\Karan12\\Documents\\PythonProjects\\MusicPlayer\\pause.png")
nextimage=PhotoImage(file="C:\\Users\\Karan12\\Documents\\PythonProjects\\MusicPlayer\\next.png")
previousimage=PhotoImage(file="C:\\Users\\Karan12\\Documents\\PythonProjects\\MusicPlayer\\previous.png")
albumimage=PhotoImage(file="C:\\Users\\Karan12\\Documents\\PythonProjects\\MusicPlayer\\keepcalm.png")

os.chdir("D:\\Dance Music\\Dance & Pop\\")
imageno=0

imagelist=[playimage,pauseimage]
f = Frame(root,bg="black",bd=0)
f.place(x=0,y=0,width=1300,height=700)
songs=[]
playlist=[]
pygame.mixer.init()


maincanvas=Canvas(f,bg="black",bd=0)
maincanvas.place(x=650,y=250,width=400,height=400,anchor=CENTER)
maincanvas.create_image(0,0,image=albumimage,anchor="nw")
root.update()

songlabel=Label(f,bg="black",fg=selectbackgroundcolour,bd=0,font=("Century Gothic",13,""),justify=CENTER)
songlabel.place(x=50,y=490,height=20,width=1200,anchor="nw")
llabel=Label(f,bg="black",fg="white",bd=0,font=("Century Gothic",10,""),padx=0,text="0 min : 00 secs")
llabel.place(x=50,y=535,height=20,width=100,anchor="nw")
rlabel=Label(f,bg="black",fg="white",bd=0,font=("Century Gothic",10,""),padx=0,text="0 min : 00 secs")
rlabel.place(x=1150,y=535,height=20,width=100,anchor="nw")
#cs - current song details.
csduration=1
cstitle=""
csindex=-1

rightframe=Frame(f,bd=0)
rightscroll=Scrollbar(rightframe,bd=0)
playlistbox=Listbox(rightframe,font=("Century Gothic",12,""),yscrollcommand=rightscroll.set,bd=0,bg=backgroundcolor,fg=foregroundcolour,selectbackground=selectbackgroundcolour,selectforeground=selectforegroundcolour)
labelr=Label(f,bg="black",fg="white",font=("Century Gothic",12,""),text="Current Playlist")

leftframe=Frame(f,bd=0)
labell=Label(f,bg="black",fg="white",font=("Century Gothic",12,""),text="All Songs")
leftscroll=Scrollbar(leftframe,bd=0)
allsongs=Listbox(leftframe,font=("Century Gothic",12,""),yscrollcommand=leftscroll.set,bd=0,bg=backgroundcolor,fg=foregroundcolour,selectbackground=selectbackgroundcolour,selectforeground=selectforegroundcolour)

s=SeekBar(x=50,y=520,height=10,width=1200,parent=f,activecolour=backgroundcolor,passivecolour="white")
b1=Button(f,text="Prev",image=previousimage,bd=0)
b2=Button(f,text="Play",image=playimage,bd=0)
b3=Button(f,text="Next",image=nextimage,bd=0)
b1.place(x=525, y=580, width=70, height=70)
b2.place(x=615, y=580, width=70, height=70)
b3.place(x=705, y=580, width=70, height=70)


def secondsToString(sec):
	return str(int(sec/60))+" min : "+str(int(sec%60))+" secs"


def playsong():
	global cstitle
	global csindex
	global csduration
	global songlabel
	global root
	global playlistbox
	global playlist
	global llabel
	songname=playlist[csindex]
	pygame.mixer.music.stop()
	pygame.mixer.music.load(songname)
	pygame.mixer.music.play()
	cstitle=songname
	for x in range(len(playlist)):
		playlistbox.selection_clear(x)
		root.update()
	playlistbox.selection_set(csindex)
	audio=mutagen.mp3.MP3(songname)
	csduration=audio.info.length
	songlabel.configure(text=songname)
	rlabel.configure(text=secondsToString(csduration))
	root.update()
	#startseekbar()
	
	
def delplsong(evt):
	global csindex
	global playlist
	global playlistbox
	global b2
	global root
	global imageno
	global rlabel
	w=evt.widget
	delindex=w.curselection()[0]
	playlist.pop(delindex)
	playlistbox.delete(0,last=END)
	i=0
	for x in playlist:
			playlistbox.insert(END,"%3s|"%(str(i+1))+x)
			i+=1
			root.update()
	if(csindex==delindex):
		pygame.mixer.music.stop()
		if(len(playlist)>0):
			csindex=(csindex)%len(playlist)
			playsong()
	if(len(playlist)==0):
		pygame.mixer.music.stop()
		songlabel.configure(text="EMPTY PLAYLIST !")
		imageno=0
		b2.configure(image=playimage)
		rlabel.config(text="0 min : 00 secs")
		root.update()
	else:
		playlistbox.selection_set(csindex)
		root.update()

	
def playnextsong(evet):
	global csindex
	csindex=(csindex+1)%len(playlist)
	playsong()

def playprevsong(evet):
	global csindex
	csindex=csindex-1
	if csindex==-1:
		csindex=len(playlist)-1
	playsong()
			
rightframe.place(x=900,y=50,width=350,height=400)
labelr.place(x=900,y=450,width=350,height=20)
playlistbox.place(x=0,y=0,width=334,height=400)
rightscroll.pack(side=RIGHT,fill=Y)
rightscroll.configure(command=playlistbox.yview)
playlistbox.bind("<<ListboxSelect>>",delplsong)

for x in os.listdir():
	if(x.endswith(".mp3")):
		try :
			songs.append(x)
		except UnicodeEncodeError:
			pass
for x in songs:
	allsongs.insert(END," %3s|"%(str(songs.index(x)+1))+x)
	
def addToPlaylist(evt):
	global playlistbox
	global playlist
	w=evt.widget
	selected=w.curselection()[0]
	try:
		playlist.index(songs[selected])
	except ValueError:
		playlist.append(songs[selected])
		playlistbox.insert(END,"%3s|"%(str(playlist.index(songs[selected])+1))+songs[selected])
		playlistbox.selection_set(csindex)
		root.update()
	
leftframe.place(x=50,y=50,width=350,height=400)
labell.place(x=50,y=450,width=350,height=20)
allsongs.place(x=0,y=0,width=334,height=400)
leftscroll.pack(side=RIGHT,fill=Y)
leftscroll.configure(command=allsongs.yview)
allsongs.bind("<<ListboxSelect>>",addToPlaylist)

def playPause(event):
	global imageno
	global csindex
	global playlist
	if(imageno==1):
		pygame.mixer.music.pause()
		imageno=(imageno+1)%2
		b2.configure(image=imagelist[imageno])
	else:
		if(len(playlist)==0):
			songlabel.configure(text="EMPTY PLAYLIST !")
		else:
			if(pygame.mixer.music.get_busy()):
				pygame.mixer.music.unpause()
			else:
				csindex=0
				playsong()
			imageno=(imageno+1)%2
			b2.configure(image=imagelist[imageno])
	root.update()
	
b2.bind("<Button-1>",playPause)
b3.bind("<Button-1>",playnextsong)
b1.bind("<Button-1>",playprevsong)

while(True):
	playtime=pygame.mixer.music.get_pos()/1000
	while(playtime<=csduration):
		playtime=pygame.mixer.music.get_pos()/1000
		p=(playtime/csduration)*100
		s.propagate(p)
		llabel.configure(text=secondsToString(playtime))
		root.update()
	if(len(playlist)>0):
		csindex=(csindex+1)%len(playlist)
		playsong()
		
root.mainloop()

