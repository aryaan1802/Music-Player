from tkinter import *
import pygame

root = Tk()
root.title('Music Player')
root.iconbitmap('C:/gui/Music_Player.ico')
root.geometry("500x400")

pygame.mixer.init()

def play():
	pygame.mixer.music.load("c:/gui/Audio/On.wav")
	pygame.mixer.music.play(loops=0)

def stop():
	pygame.mixer.music.stop()

my_button = Button(root, text="Play Music", font=("Arial",28 ), command=play)
my_button.pack(pady=20)

stop_button = Button(root, text="Stop Music", command=stop)
stop_button.pack(pady=20)

root.mainloop() 
