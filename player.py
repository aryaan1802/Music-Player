from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('Music Player - Mini Project')
root.iconbitmap('c:/gui/Music_Player.ico')
root.geometry("500x300")

# Initialize Pygame Mixer To Start Music Player
pygame.mixer.init()

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
	#Removing Current Selected Song From The Music Player
	song_list.delete(ANCHOR)
	#Stop The Music, If It's Playing
	pygame.mixer.music.stop()

#Remove All Songs Function
def remove_song2():
	#Removing All Songs From The Music Player
	song_list.delete(0, END)
	#Stop The Music, If It's Playing
	pygame.mixer.music.stop( )

#PLAY Button : Play Selected Song on the Song List 
def play():
	song = song_list.get(ACTIVE)
	song = f'C:/gui/Audio/{song}.wav'

	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

#STOP Button : Stop Playing Current Song
def stop():
	pygame.mixer.music.stop()
	song_list.selection_clear(ACTIVE)

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

#Create Playlist Box
song_list = Listbox(root, bg="black", fg="green", width=50, selectbackground="gray", selectforeground="black")
song_list.pack(pady=20)

#Define Player Control Button Images
back_btn_img = PhotoImage(file='c:/gui/Images/back50.png')
forward_btn_img = PhotoImage(file='c:/gui/Images/forward50.png')
play_btn_img = PhotoImage(file='c:/gui/Images/play50.png')
pause_btn_img = PhotoImage(file='c:/gui/Images/pause50.png')
stop_btn_img =  PhotoImage(file='c:/gui/Images/stop50.png')

#Create Player Control Frame
controls_frame = Frame(root)
controls_frame.pack()

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

root.mainloop()