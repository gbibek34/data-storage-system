from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image
from Queries import Queries
import os
os.chdir(r"E:\Assignment\Sem 2\Algorithm\Data Storage System")

class NotesManager:
    def __init__(self, notes):
        self.con = Queries()
        self.note_id_val = StringVar()
        # Images
        self.add_image = ImageTk.PhotoImage(Image.open("Icons/Add.png").resize((50, 50)))
        self.update_image = ImageTk.PhotoImage(Image.open("Icons/Update.png").resize((50, 50)))
        self.delete_image = ImageTk.PhotoImage(Image.open("Icons/Delete.png").resize((50, 50)))
        self.reset_image = ImageTk.PhotoImage(Image.open("Icons/Reset.png").resize((50, 50)))
        # Frames
        self.frame1 = Frame(notes, relief=RIDGE, bd=8)
        self.frame1.place(x=10, y=10, width=1235, height=500)
        self.frame2 = Frame(self.frame1, relief=RIDGE, bd=5)
        self.frame2.place(x=0, y=0, width=200, height=485)
        # Label
        self.note_id_lbl = Label(self.frame1, text="Note ID:", font=('verdana', 12))
        self.note_id_lbl.place(x=230, y=10)
        self.note_lbl = Label(self.frame1, text="Note:", font=('verdana', 12))
        self.note_lbl.place(x=230, y=50)
        # Entry
        self.note_id_ent = Entry(self.frame1, font=('arial', 12), textvariable=self.note_id_val, state="readonly")
        self.note_id_ent.place(x=320, y=12)
        self.note_ent = Text(self.frame1, width=100, height=20, font=('arial', 12))
        self.note_ent.place(x=300, y=55)
        # Buttons
        self.add_btn = Button(self.frame1, relief=FLAT, image=self.add_image, command=self.add_note)
        self.add_btn.place(x=550, y=420)
        self.update_btn = Button(self.frame1, relief=FLAT, image=self.update_image, command=self.update_note)
        self.update_btn.place(x=650, y=420)
        self.delete_btn = Button(self.frame1, relief=FLAT, image=self.delete_image, command=self.delete_note)
        self.delete_btn.place(x=750, y=420)
        self.reset_btn = Button(self.frame1, relief=FLAT, image=self.reset_image, command=self.reset_note)
        self.reset_btn.place(x=850, y=420)
        # TreeView
        self.scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.note_tbl = ttk.Treeview(self.frame2, columns=("note"), xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.note_tbl.yview, bg='#9BC01C')
        self.note_tbl.heading("note", text="Note Number")
        self.note_tbl['show'] = 'headings'
        self.note_tbl.column("note")
        self.note_tbl.pack(fill=BOTH, expand='1')
        self.insert_note()
#Methods
    def add_note(self):
        print(self.note_ent.get("1.0","end"))
        if self.note_ent.get("1.0","end")=='':
            tkinter.messagebox.showerror('Error','Dont leave the field empty.')
        else:
            self.con.add_note(self.note_ent.get("1.0","end"))
            self.insert_note()
            self.reset_note()

    def update_note(self):
        if self.note_ent.get("1.0","end")=='':
            tkinter.messagebox.showerror('Error','Dont leave the field empty.')
        else:
            self.con.update_note(self.note_ent.get("1.0","end"), self.note_id_ent.get())
            self.insert_note()
            self.reset_note()

    def delete_note(self):
        self.con.delete_note(self.note_id_ent.get())
        self.insert_note()
        self.reset_note()

    def reset_note(self):
        self.note_id_val.set('')
        self.note_ent.delete("1.0","end")

    def insert_note(self):
        data = self.con.fetch_note()
        self.note_tbl.delete(*self.note_tbl.get_children())
        for i in data:
            self.note_tbl.insert("","end", value=(i[0],i[1]))
        self.note_tbl.bind('<Double-1>',self.select_note)

    def select_note(self, event):
        self.row = self.note_tbl.item(self.note_tbl.selection(), "values")
        self.fill_note()

    def fill_note(self):
        self.reset_note()
        self.note_id_val.set(self.row[0])
        self.note_ent.insert("0.0",self.row[1])