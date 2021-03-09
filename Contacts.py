from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image
from Queries import Queries
import os
os.chdir(r"E:\Assignment\Sem 2\Algorithm\Data Storage System")

class ContactManager:
    def __init__(self, contacts):
        self.con = Queries()
        self.contact_id_val = StringVar()
        #Images
        self.add_image = ImageTk.PhotoImage(Image.open("Icons/Add.png").resize((50, 50)))
        self.update_image = ImageTk.PhotoImage(Image.open("Icons/Update.png").resize((50, 50)))
        self.delete_image = ImageTk.PhotoImage(Image.open("Icons/Delete.png").resize((50, 50)))
        self.reset_image = ImageTk.PhotoImage(Image.open("Icons/Reset.png").resize((50, 50)))
        #Frames
        self.frame1 = Frame(contacts, relief=RIDGE, bd=8)
        self.frame1.place(x=10, y=10, width=430, height=500)
        self.frame2 = Frame(contacts)
        self.frame2.place(x=450, y=10, width=800, height=500)
        #Labels
        self.id_lbl = Label(self.frame1, text="Contact ID:", font=('verdana', 12))
        self.id_lbl.place(x=10, y=10)
        self.fname_lbl = Label(self.frame1, text="First Name:", font=('verdana', 12))
        self.fname_lbl.place(x=10, y=50)
        self.lname_lbl = Label(self.frame1, text="Last Name:", font=('verdana', 12))
        self.lname_lbl.place(x=10, y=90)
        self.group_lbl = Label(self.frame1, text="Group:", font=('verdana', 12))
        self.group_lbl.place(x=10, y=130)
        self.number_lbl = Label(self.frame1, text="Phone:", font=('verdana', 12))
        self.number_lbl.place(x=10, y=170)
        self.email_lbl = Label(self.frame1, text="E-mail:", font=('verdana', 12))
        self.email_lbl.place(x=10, y=210)
        self.address_lbl = Label(self.frame1, text="Address:", font=('verdana', 12))
        self.address_lbl.place(x=10, y=250)
        #Entries
        self.contact_id_ent = Entry(self.frame1, font=('arial', 12), width=22, textvariable=self.contact_id_val,
                            state="readonly")
        self.contact_id_ent.place(x=120, y=10)
        self.fname_ent = Entry(self.frame1, font=('arial', 12), width=22)
        self.fname_ent.place(x=120, y=50)
        self.lname_ent = Entry(self.frame1, font=('arial', 12), width=22)
        self.lname_ent.place(x=120, y=90)
        self.group_ent = ttk.Combobox(self.frame1, font=('arial', 12), width=20, state='readonly')
        self.group_ent['values']=('Work',"Home","College")
        self.group_ent.place(x=120,y=130)
        self.number_ent = Entry(self.frame1, font=('arial', 12), width=22)
        self.number_ent.place(x=120,y=170)
        self.email_ent = Entry(self.frame1, font=('arial', 12), width=22)
        self.email_ent.place(x=120,y=210)
        self.address_ent = Entry(self.frame1, font=('arial', 12), width=22)
        self.address_ent.place(x=120,y=250)
        #Buttons
        self.add_btn = Button(self.frame1, relief=FLAT, image=self.add_image, command=self.add_contact)
        self.add_btn.place(x=100, y=320)
        self.edit_btn = Button(self.frame1, relief=FLAT, image=self.update_image, command=self.update_contact)
        self.edit_btn.place(x=240, y=320)
        self.delete_btn = Button(self.frame1, relief=FLAT, image=self.delete_image, command=self.delete_contact)
        self.delete_btn.place(x=100, y=400)
        self.reset_btn = Button(self.frame1, relief=FLAT, image=self.reset_image, command=self.reset_contact)
        self.reset_btn.place(x=240, y=400)
        #Treeview
        self.scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.contact_tbl = ttk.Treeview(self.frame2,
                                       columns=("fname", "lname", "group", "number", "email", "address"),
                                       xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.contact_tbl.yview, bg='#9BC01C')
        self.contact_tbl.heading("fname",text="First Name")
        self.contact_tbl.heading("lname",text="Last Name")
        self.contact_tbl.heading("group",text="Group")
        self.contact_tbl.heading("number", text="Phone No")
        self.contact_tbl.heading("email", text="E-mail")
        self.contact_tbl.heading("address", text="Address")
        self.contact_tbl['show']='headings'
        self.contact_tbl.column("fname", width=30)
        self.contact_tbl.column("lname", width=30)
        self.contact_tbl.column("group", width=30)
        self.contact_tbl.column("number", width=30)
        self.contact_tbl.column("email", width=60)
        self.contact_tbl.column("address", width=60)
        self.contact_tbl.pack(fill=BOTH, expand='1')
        self.insert_contact()
#Methods
    def add_contact(self):
        if self.fname_ent.get()=='' or self.lname_ent.get()=='' or self.group_ent.get()=='' or \
                self.number_ent.get()=='' or self.email_ent.get()=='' or self.address_ent.get()=='':
            tkinter.messagebox.showerror('Error','Dont leave the fields empty.')
        else:
            self.con.add_contact(self.fname_ent.get(),self.lname_ent.get(), self.group_ent.get(),
                               self.number_ent.get(), self.email_ent.get(), self.address_ent.get())
            self.insert_contact()
            self.reset_contact()

    def update_contact(self):
        if self.fname_ent.get()=='' or self.lname_ent.get()=='' or self.group_ent.get()=='' or \
                self.number_ent.get()=='' or self.email_ent.get()=='' or self.address_ent.get()=='':
            tkinter.messagebox.showerror('Error','Dont leave the fields empty.')
        else:
            self.con.update_contact(self.fname_ent.get(),self.lname_ent.get(), self.group_ent.get(),
                               self.number_ent.get(), self.email_ent.get(), self.address_ent.get(), 
                               self.contact_id_ent.get())
            self.insert_contact()
            self.reset_contact()

    def delete_contact(self):
        self.con.delete_contact(self.contact_id_ent.get())
        self.insert_contact()
        self.reset_contact()

    def reset_contact(self):
        self.contact_id_val.set('')
        self.fname_ent.delete(0,END)
        self.lname_ent.delete(0,END)
        self.group_ent.set('')
        self.number_ent.delete(0,END)
        self.email_ent.delete(0,END)
        self.address_ent.delete(0,END)

    def insert_contact(self):
        data = self.con.fetch_contact()
        self.contact_tbl.delete(*self.contact_tbl.get_children())
        for i in data:
            self.contact_tbl.insert("","end", value=(i[1],i[2],i[3],i[4],i[5],i[6],i[0]))
        self.contact_tbl.bind('<Double-1>',self.select_contact)

    def select_contact(self, event):
        self.row = self.contact_tbl.item(self.contact_tbl.selection(), "values")
        self.fill_contact()

    def fill_contact(self):
        self.reset_contact()
        self.contact_id_val.set(self.row[6])
        self.fname_ent.insert(0,self.row[0])
        self.lname_ent.insert(0,self.row[1])
        self.group_ent.set(self.row[2])
        self.number_ent.insert(0,self.row[3])
        self.email_ent.insert(0,self.row[4])
        self.address_ent.insert(0,self.row[5])
