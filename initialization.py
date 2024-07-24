import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

# Root

root = tk.Tk()
root.title('To-Do List')
root.geometry('350x500')
root.resizable(False, True)
root.config(background='grey')

# Frames & Widgets

head = tk.Frame(width='350', height='70', bg='#595959')
head.place(x=0, y=0)

body = tk.Frame(width='300', height='400', bg='#969696')
body.place(x=0, y=80)

progFrame = tk.Frame(width='350',height='30',bg='green')
progFrame.place(x=0,y=50)

noteEntry = tk.Entry(head,width=30,font=('gill sans',10, 'bold'))
noteEntry.place(x=25, y=15)

prog = tk.Label(progFrame, text='0 out of 0')
prog.place(x=150,y=5)


# Attachements

add_img = ImageTk.PhotoImage(Image.open("textures/add.png").resize((30, 30)))
dots_img = ImageTk.PhotoImage(Image.open("textures/dots.png").resize((32, 32)))
edit_img = ImageTk.PhotoImage(Image.open("textures/edit.png").resize((22, 22)))
delete_img = ImageTk.PhotoImage(Image.open("textures/delete.png").resize((22, 22)))
bg_image = ImageTk.PhotoImage(Image.open("textures/back.png").resize((600, 600)))