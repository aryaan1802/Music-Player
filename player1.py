from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.wave import WAVE
import tkinter.ttk as ttk

root = Tk()
root.title('Music Player - Mini Project')
root.iconbitmap('c:/gui/Music_Player.ico')
root.geometry("500x450")

# Initialize Pygame Mixer To Start Music Player
pygame.mixer.init()

#Grab Song Time Length
def play_time():
	#Check For Double Loops Running For Two Songs' Sliders At Same Time
	if stopped:
		return
	#Grab Current Song Lapsed Time
	current_time = pygame.mixer.music.get_pos() / 1000

	#Throw Up Temporary Label To Get Data
	#slider_label.config(text=f'Slider: {int(my_slider.get())} and Song Position: {int(current_time)}')

	#Converting Time Elapsed To The Time Format
	converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))

	#Getting The Current Playing Song
	current_song = song_list.curselection()
	song = song_list.get(current_song)
	song = f'C:/gui/Audio/{song}.wav'

	#Get Song Using Mutagen
	song_mut = WAVE(song)
	#Get Song Length
	global song_length
	song_length = song_mut.info.length

	#Convert Time Length of Song To Time Format
	converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))

	#Increase Current Time By 1 Second
	current_time+=1

	if int(my_slider.get()) == int(song_length):
		status_bar.config(text=f'Time Elapsed: {converted_song_length} of {converted_song_length} ')

	elif paused:
		pass

	elif int(my_slider.get()) == int(current_time):
		#Slider Has Not Been Moved By Us Externally
			#Update Slider To Position
			slider_position =  int(song_length)
			my_slider.config(to=slider_position, value=int(current_time))
	else:
		#Slider Has Been Moved By Us Externally
			#Update Slider To Position
			slider_position =  int(song_length)
			my_slider.config(to=slider_position, value=int(my_slider.get()))

			#Converting Time Elapsed Based On The Slider's Position To The Time Format
			converted_current_time = time.strftime('%M:%S', time.gmtime(my_slider.get()))

			#Output Time To The Status Bar
			status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length} ')

			#Move This Slider Position Along By One Position
			next_time = int(my_slider.get()) + 1
			my_slider.config(value=next_time)

	#Updating Slider Position Value to Current Time Value
	#my_slider.config(value=int(current_time))

	#Updates Time Of The Song Currently Being Played
	status_bar.after(1000, play_time)

#Add One Song Function
def add_song1():
	song = filedialog.askopenfilename(initialdir='c:/gui/Audio/', title="Choose A Song", filetypes=(("wav Files", "*.wav"), ))
	#Strip Out Directory Name and .wav text so that only song name appears
	song = song.replace("C:/gui/Audio/", "")
	song = song.replace(".wav", "")
	#Add Song To Song List
	song_list.insert(END, song)

#Add Many Songs Function
def add_song2():
	songs = filedialog.askopenfilenames(initialdir='c:/gui/Audio/', title="Choose Songs", filetypes=(("wav Files", "*.wav"), ))
	#Loop Through Song List And Replace Directory Info and wav For Each Song
	for song in songs:
		song = song.replace("C:/gui/Audio/", "")
		song = song.replace(".wav", "")
		#Add Song To Song List
		song_list.insert(END, song)

#Remove One Song Function
def remove_song1():
	stop()
	#Removing Current Selected Song From The Music Player
	song_list.delete(ANCHOR)
	#Stop The Music, If It's Playing
	pygame.mixer.music.stop()

#Remove All Songs Function
def remove_song2():
	stop()
	#Removing All Songs From The Music Player
	song_list.delete(0, END)
	#Stop The Music, If It's Playing
	pygame.mixer.music.stop( )

#PLAY Button : Play Selected Song on the Song List 
def play():
	#Set Stopped Variable to False So That Song Can Play
	global stopped
	stopped = False
	song = song_list.get(ACTIVE)
	song = f'C:/gui/Audio/{song}.wav'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	#Calling The Play-Time Function To Print Length Of Each Song
	play_time()

	#Update Slider To Position
	#slider_position =  int(song_length)
	#my_slider.config(to=slider_position, value=0)

	#Getting The Current Song
	#current_vol = pygame.mixer.music.get_volume()
	#slider_label.config(text=int(current_vol * 100))

	#Getting The Current Volume
	current_vol = pygame.mixer.music.get_volume()

	#Multiplying The Current Volume By 100 So That Range Changes From 0 to 1 To 1 to 100
	current_vol = current_vol * 100
	#slider_label.config(text=current_vol * 100)

	#Changing The Volume Meter Image
	if int(current_vol) < 1:
		volume_meter.config(image=vol0)
	elif int(current_vol) > 0 and int(current_vol) <= 25:
		volume_meter.config(image=vol1)
	elif int(current_vol) >= 25 and int(current_vol) <= 50:
		volume_meter.config(image=vol2)
	elif int(current_vol) >= 50 and int(current_vol) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_vol) >= 75 and int(current_vol) <= 100:
		volume_meter.config(image=vol4)

#Create Global Stop Variable
global stopped
stopped = False

#STOP Button : Stop Playing Current Song
def stop():
	#Reset The Slider Position And Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)

	#Stop The Song From Playing
	pygame.mixer.music.stop()
	song_list.selection_clear(ACTIVE)

	#Clear The Status Bar
	status_bar.config(text='')

	#Set Stop Variable To True
	global stopped
	stopped = True

#Create Global Pause Variable
global paused
paused = False

#PAUSE Button : Pause and Unpause The Current Song
def pause(is_paused):
	global paused
	paused = is_paused

	if paused:
		#Unpause
		pygame.mixer.music.unpause()
		paused = False
	else:
		#Pause
		pygame.mixer.music.pause()
		paused = True

#FORWARD Button : Play The Next Song In The Playlist
def forward_song():
	#Reset The Slider Position And The Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)

	#Getting The Current Song's Tuple Number 
	next_one = song_list.curselection()

	#Add One To The Current Song's Tuple Number To Play The Next Song
	#print(next_one)
	#print(next_one[0])
	
	next_one = next_one[0]+1
	song = song_list.get(next_one)
	song = f'C:/gui/Audio/{song}.wav'
	print(song)
	
	#Load And Play The Next Song
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)
	
	#Move ACTIVE Bar In The Playlist SongList
	song_list.selection_clear(0, END)
	
	#Activate The New Song Bar
	song_list.activate(next_one)
	
	#Set ACTIVE Bar To The Next Song
	song_list.selection_set(next_one)

#BACK BUTTON : Play The Previous Song In The Playlist
def back_song():
	#Reset Slider Position And The Status Bar
	status_bar.config(text='')
	my_slider.config(value=0)

	#Getting The Current Song's Tuple Number
	next_one = song_list.curselection()

	#Add One To The Current Song's Tuple Number To Play The Next Song
	#print(next_one)
	#print(next_one[0])

	next_one = next_one[0]-1
	song = song_list.get(next_one)
	song = f'C:/gui/Audio/{song}.wav'
	print(song)

	#Load And Play The Next Song
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

	#Move ACTIVE Bar In The Playlist Songlist
	song_list.selection_clear(0, END)

	#Activate The New Song Bar
	song_list.activate(next_one)

	#Set ACTIVE Bar To The Next Song
	song_list.selection_set(next_one)

#Create Slider Function
def slide(x):
	#slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
	song = song_list.get(ACTIVE)
	song = f'C:/gui/Audio/{song}.wav'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0, start=int(my_slider.get()))

#Create Volume Function
def volume(x):
	pygame.mixer.music.set_volume(vol_slider.get())

	#Getting The Current Volume
	current_vol = pygame.mixer.music.get_volume()

	#Multiplying The Current Volume By 100 So That Range Changes From 0 to 1 To 1 to 100
	current_vol =  current_vol * 100
	#slider_label.config(text=int(current_vol * 100))

	#Changing The Volume Meter Image
	if int(current_vol) < 1:
		volume_meter.config(image=vol0)
	elif int(current_vol) > 0 and int(current_vol) <=25:
		volume_meter.config(image=vol1)
	elif int(current_vol) >= 25 and int(current_vol) <=50:
		volume_meter.config(image=vol2)
	elif int(current_vol) >= 50 and int(current_vol) <= 75:
		volume_meter.config(image=vol3)
	elif int(current_vol) >=75 and int(current_vol) <=100:
		volume_meter.config(image=vol4)

#Create Master Frame
master_frame = Frame(root)
master_frame.pack(pady=20)

#Create Playlist Box
song_list = Listbox(master_frame, bg="black", fg="green", width=50, selectbackground="gray", selectforeground="black")
song_list.grid(row=0, column=0)

#Define Player Control Button Images
back_btn_img = PhotoImage(file='c:/gui/Images/back50.png')
forward_btn_img = PhotoImage(file='c:/gui/Images/forward50.png')
play_btn_img = PhotoImage(file='c:/gui/Images/play50.png')
pause_btn_img = PhotoImage(file='c:/gui/Images/pause50.png')
stop_btn_img =  PhotoImage(file='c:/gui/Images/stop50.png')

#Define Volume Control Images
global vol0
global vol1
global vol2
global vol3
global vol4
vol0 = PhotoImage(file='c:/gui/Images/vol0-50p.png')
vol1 = PhotoImage(file='c:/gui/Images/vol25-50p.png')
vol2 = PhotoImage(file='c:/gui/Images/vol50-50p.png')
vol3 = PhotoImage(file='c:/gui/Images/vol75-50p.png')
vol4 = PhotoImage(file='c:/gui/Images/vol100-50p.png')

#Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=20)

#Create Volume Meter
volume_meter = Label(master_frame, image=vol0)
volume_meter.grid(row=1, column=1, padx=12)

#Create Volume Label Frame
volume_frame = LabelFrame(master_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=25)

#Create Player Control Buttons
back_btn = Button(controls_frame, image=back_btn_img, borderwidth=0, command=back_song)
forward_btn = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=forward_song)
play_btn =  Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_btn =  Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_btn =  Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)

back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=1, padx=10)
play_btn.grid(row=0, column=2, padx=10)
pause_btn.grid(row=0, column=3, padx=10)
stop_btn.grid(row=0, column=4, padx=10)

#Create Menu To Add/Remove Songs
my_menu = Menu(root)
root.config(menu=my_menu)

#Add 'Add Songs Menu'
add_songs_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_songs_menu)
#Add One Song To The Music Player
add_songs_menu.add_command(label="Add One Song To The Music Player", command=add_song1)
#Add Many Songs To The Music Player
add_songs_menu.add_command(label="Add Many Songs To The Music Player", command=add_song2)

#Add 'Remove Songs Menu'
remove_songs_menu =Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_songs_menu)
#Remove One Song From The Music Player
remove_songs_menu.add_command(label="Remove One Song From The Music Player", command=remove_song1)
#Remove All Songs From The Music Player
remove_songs_menu.add_command(label="Remove All Songs From The Music Player", command=remove_song2)

#Create Status Bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

#Create Music Position Slider
my_slider = ttk.Scale(master_frame, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
my_slider.grid(row=2, column=0, pady=10) 

#Create Volume Position Slider
vol_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume, length=125)
vol_slider.pack(pady=10,)

#Create Temporary Slider Label
#slider_label = Label(root, text="0")
#slider_label.pack(pady=10)

root.mainloop()