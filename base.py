import tkinter as tk
import tkinter.ttk as ttk
import json
from initialization import *


class NoteBase:
    notes_lst = []
    def __init__(self, txt):
        NoteBase.notes_lst.append(self)
        self.txt = txt
        self.noteFrame = tk.Frame(body, height=60, width=350, bg='#828282')
        self.on_image = tk.PhotoImage(width=48, height=24)
        self.off_image = tk.PhotoImage(width=48, height=24)
        self.on_image.put(("green",), to=(0, 0, 23, 23))
        self.off_image.put(("red",), to=(24, 0, 47, 23))
        self.var1 = tk.IntVar(value=0)
        ttk.Style().layout('no_indicatoron.TCheckbutton',
                           [('Checkbutton.padding', {'sticky': 'nswe', 'children': [
                               ('Checkbutton.focus', {'side': 'left', 'sticky': 'w',
                                                      'children': [('Checkbutton.label', {'sticky': 'nswe'})]})]})])
        self.label = tk.Label(self.noteFrame, text=txt, height=3,width=23,wraplength=215,font=('Lucida Console',10, 'bold'), bg='#828282')
        self.cb = ttk.Checkbutton(self.noteFrame, image=self.off_image, onvalue=1, offvalue=0,
                                   variable=self.var1, style='no_indicatoron.TCheckbutton', command=self.cb_state)
        self.delButton = tk.Button(self.noteFrame, text='del', command=self.delNote,image=delete_img)
        self.editButton = tk.Button(self.noteFrame, text='Edit', command=lambda:self.editNote(),image=edit_img)

    def cb_state(self):
        if self.cb.instate(['!disabled', 'selected']):
            self.cb['image'] = self.on_image
        else:
            self.cb['image'] = self.off_image
        progress()
        saveNotes()

    def delNote(self):
        self.noteFrame.pack_forget()
        NoteBase.notes_lst.remove(self)
        progress()
        saveNotes()

    def editNote(self):
        global editEntry
        editWindow = tk.Toplevel(root)
        editWindow.title('Enter text')
        editWindow.config(background='#D1D1D1')
        editWindow.resizable(False, False)
        editLabel = tk.Label(editWindow, text='Edit note : ', bg='#D1D1D1')
        editLabel.pack(pady=15)
        editEntry = tk.Entry(editWindow)
        editEntry.pack(padx=20, pady=5)
        editEntry.insert(0, self.label.cget("text"))


        def applyEdit():
            for note in NoteBase.notes_lst:
                if note.label.cget("text") == self.txt:
                    note.label.config(text=editEntry.get())
                    self.txt = editEntry.get()
                    break
            editWindow.destroy()
            saveNotes()


        okButton = tk.Button(editWindow,text='ok',command=lambda:applyEdit(),padx=15,relief='groove',bg='#999999')
        okButton.pack(pady=20)

    def isON(self):
        return self.var1.get() == 1

class Note(NoteBase):
    def __init__(self, txt):
        super().__init__(txt)

    def create_note(self):
        self.noteFrame.pack(pady=10)
        self.label.place(x=1, y=10) 
        self.cb.place(x=225, y=17)
        self.delButton.place(x=318, y=18)
        self.editButton.place(x=285,y=18)
        progress()

class Buttons:
    addButton = tk.Button(head, text='Add', command=lambda: addNote(noteEntry.get()),image=add_img)
    addButton.place(x=250, y=7)

    optionsButton = tk.Menubutton(head, text='Options',image=dots_img)
    optionsButton.place(x=295, y=7)
    ss = tk.Menu(optionsButton, tearoff=0)
    optionsButton['menu'] = ss
    ss.add_command(label='Credits',command=lambda:fetchCredits())
    ss.add_command(label='Delete all', command=lambda:delAll())



# Functions
def saveNotes():
    notes_data = []
    for note in NoteBase.notes_lst:
        note_data = {
            'text': note.label.cget("text"),
            'checked': note.var1.get() == 1
        }
        notes_data.append(note_data)

    with open('config.txt', 'w') as file:
        json.dump(notes_data, file)

def loadNotes():
    try:
        with open('config.txt', 'r') as file:
            notes_data = json.load(file)
            for note_data in notes_data:
                note = Note(note_data['text'])
                note.create_note()
                if note_data['checked']:
                    note.cb.invoke()  # Check the checkbox if 'checked' is True
    except FileNotFoundError:
        pass

def addNote(txt):
    if noteEntry.get() == '':
        print("Please Enter a text")
        pass
    else:
        note = Note(txt)
        note.create_note()
        saveNotes()  # Save notes to config file
        noteEntry.delete(0, tk.END)

def delAll():
    body.destroy()
    makeBody()
    NoteBase.notes_lst = []
    progress()
    saveNotes()  # Save notes to config file

def progress():
    finished = [n for n in NoteBase.notes_lst if n.isON()]
    prog.config(text=f'{len(finished)} out of {len(NoteBase.notes_lst)}')

def makeBody():
    global body
    body = tk.Frame(width='300', height='400', bg='#969696')
    body.place(x=0, y=80)

def fetchCredits():
    credits_window = tk.Toplevel(root)
    credits_window.title('Credits')
    credits_window.config(background='#D1D1D1')
    credits_window.resizable(False,False)
    
    bg_label = tk.Label(credits_window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)

    info_1 = tk.Label(credits_window, text="Developer: Seif Eldeen Nasser", font=("Helvetica", 14), bg='#D1D1D1')
    info_1.pack(pady=10)
    info_2 = tk.Label(credits_window, text="sayfeldinn@gmail.com", font=("Helvetica", 14), bg='#D1D1D1')
    info_2.pack(pady=5)
    info_3 = tk.Label(credits_window, text="linkedin.com/in/sayfeldinn", font=("Helvetica", 14), bg='#D1D1D1')
    info_3.pack(pady=5)
    info_4 = tk.Label(credits_window, text="'To-Do List' is a project to write down and track daily tasks\nbased on developing the skills and basics learned through CS50", font=("Helvetica", 10), bg='#D1D1D1')
    info_4.pack(pady=5)
    
