import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint, shuffle
import pygame

def music_down():
    global music_down
    if music_down:
        music_down = False
        pygame.mixer.music.pause()
        return 0
    music_down = True
    pygame.mixer.music.unpause()


def Set(a):
    if len(str(a))==6:
        set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        outnumber1 = int(a[3:6])
        outnumber2 = int(a[0:3])
        outnumber3 = str(outnumber1+outnumber2)
        if len(outnumber3)==3:
            outnumber3="0"+outnumber3
        outnumber1 = str(outnumber1)+set[randint(0,len(set))]+set[randint(0,len(set))]
        outnumber2 = str(outnumber2)+set[randint(0,len(set))]+set[randint(0,len(set))]
        return(outnumber1+"-"+outnumber2+" "+outnumber3)
    else:
        return("неверные данные")
root = Tk()
root.title("Game")
#root.geometry("1920x1080") 
root.geometry("1920x1080") 
background_image=tk.PhotoImage(file="game.png")#c:/Users/e5470/Desktop/Учёба/python/Lab-3/
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def show_message():
    label["text"] = Set(entry.get())     # получаем введенный текст

entry = ttk.Entry()
entry.place(x=600, y=20)
  
btn = ttk.Button(text="Сгенерировать ключ", command=show_message)
btn.place(x=750, y=20)
 
label = ttk.Label()
label.place(x=600, y=40)

canvas = Canvas(bg="white", width=156, height=20)
canvas.place(x=400, y=20)
canvas.create_text(78, 10, text="введите DEC-число 6 знаков", fill="#004D40")

button_Music_down = ttk.Button(root, text="Поставить музыку на паузу", command=music_down)
button_Music_down_canvas = canvas.create_window(0, 23, anchor="nw", window=button_Music_down)

# Play music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("1.mp3")#c:/Users/e5470/Desktop/Учёба/python/Lab-3/
pygame.mixer.music.play(-1)

root.mainloop()