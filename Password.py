from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk, Image
from Queries import Queries
import os
os.chdir(r"E:\Assignment\Sem 2\Algorithm\Data Storage System")

class PasswordManager:
    def __init__(self, password):
        self.con = Queries()
        self.count = 0
        #Images
        self.show_image = ImageTk.PhotoImage(Image.open("Icons/Show.png").resize((20, 20)))
        self.add_image = ImageTk.PhotoImage(Image.open("Icons/Add.png").resize((50, 50)))
        self.update_image = ImageTk.PhotoImage(Image.open("Icons/Update.png").resize((50, 50)))
        self.delete_image = ImageTk.PhotoImage(Image.open("Icons/Delete.png").resize((50, 50)))
        self.reset_image = ImageTk.PhotoImage(Image.open("Icons/Reset.png").resize((50, 50)))
        #Frames
        self.frame1 = Frame(password, relief=RIDGE, bd=8)
        self.frame1.place(x=10, y=10, width=430, height=500)
        self.frame2 = Frame(password, relief=RIDGE, bd=1)
        self.frame2.place(x=650, y=10, width=600, height=500)
        self.frame3 = Frame(password, relief=RIDGE, bd=1)
        self.frame3.place(x=450, y=10, width=200, height=500)
        self.category_frame = Frame(self.frame1, relief=RIDGE, bd=1)
        self.category_frame.place(x=0, y=0, width=415, height=200)
        self.entry_frame = Frame(self.frame1, relief=RIDGE, bd=1)
        self.entry_frame.place(x=0, y=200, width=415, height=285)
        #Lables
        self.create_lbl = Label(self.category_frame, text="Create Category", font=('verdana',12))
        self.create_lbl.place(x=140, y=10)
        self.account_lbl = Label(self.entry_frame, text="Account Name:", font=('verdana',12))
        self.account_lbl.place(x=20, y=20)
        self.category_lbl = Label(self.entry_frame, text="Category :", font=('verdana',12))
        self.category_lbl.place(x=20, y=60)
        self.username_lbl = Label(self.entry_frame, text="Username\n/E-mail :", font=('verdana',12))
        self.username_lbl.place(x=20, y=100)
        self.passowrd_lbl = Label(self.entry_frame, text="Password :", font=('verdana',12))
        self.passowrd_lbl.place(x=20, y=155)
        #Entries
        self.create_ent = Entry(self.category_frame, font=('verdana', 12))
        self.create_ent.place(x=110, y=80)
        self.account_ent = Entry(self.entry_frame, font=('verdana', 12))
        self.account_ent.place(x=170, y=20)
        self.category_ent = ttk.Combobox(self.entry_frame, font=('arial', 12), width=20, state='readonly')
        self.category_ent['values']=()
        self.category_ent.place(x=170, y=60)
        self.username_ent = Entry(self.entry_frame, font=('verdana', 12))
        self.username_ent.place(x=170, y=100)
        self.password_ent = Entry(self.entry_frame, font=('verdana', 12), show='*')
        self.password_ent.place(x=170, y=155)
        self.category()
        #Buttons
        self.show_btn = Button(self.entry_frame, relief=FLAT, image=self.show_image, command=self.show)
        self.show_btn.image = self.show_image
        self.show_btn.place(x=380,y=153)
        self.add_c_btn = Button(self.category_frame, relief=FLAT, image=self.add_image, command=self.add_category)
        self.add_btn = Button(self.entry_frame, relief=FLAT, image=self.add_image, command=self.add_password)
        self.add_btn.image = self.add_image
        self.add_c_btn.place(x=140, y=120)
        self.add_btn.place(x=20, y=220)
        self.update_btn = Button(self.entry_frame, relief=FLAT, image=self.update_image, command=self.update_password)
        self.update_btn.image = self.update_image
        self.update_btn.place(x=120, y=220)
        self.delete_c_btn = Button(self.category_frame, relief=FLAT, image=self.delete_image, command=self.delete_category)
        self.delete_btn = Button(self.entry_frame, relief=FLAT, image=self.delete_image, command=self.delete_password)
        self.delete_btn.image = self.delete_image
        self.delete_c_btn.place(x=220, y=120)
        self.delete_btn.place(x=220, y=220)
        self.reset_btn = Button(self.entry_frame, relief=FLAT, image=self.reset_image, command=self.reset_password)
        self.reset_btn.image = self.reset_image
        self.reset_btn.place(x=320, y=220)
        #Treeview1
        self.scroll_y = Scrollbar(self.frame3, orient=VERTICAL)
        self.category_tbl = ttk.Treeview(self.frame3,
                                         columns=("category"),
                                         xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.category_tbl.yview, bg='#9BC01C')
        self.category_tbl.heading("category", text="Category")
        self.category_tbl['show'] = 'headings'
        self.category_tbl.column("category", width=30)
        self.category_tbl.pack(fill=BOTH, expand='1')
        self.insert_category()
        #Treeview2
        self.scroll_y = Scrollbar(self.frame2, orient=VERTICAL)
        self.password_tbl = ttk.Treeview(self.frame2,
                                        columns=("account", "category", "username"),
                                        xscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill='y')
        self.scroll_y.config(command=self.password_tbl.yview, bg='#9BC01C')
        self.password_tbl.heading("account", text="Account")
        self.password_tbl.heading("category", text="Category")
        self.password_tbl.heading("username", text="Username / Email")
        self.password_tbl['show'] = 'headings'
        self.password_tbl.column("account", width=30)
        self.password_tbl.column("category", width=30)
        self.password_tbl.column("username", width=30)
        self.password_tbl.pack(fill=BOTH, expand='1')
        self.insert_password()
#Methods
    def add_category(self):
        data = self.con.fetch_category()
        category = self.create_ent.get()
        result = self.binary_search(data, category)
        if result != -1:
            tkinter.messagebox.showerror('Error', 'Category already exists')
        else:
            if self.create_ent.get()=='':
                tkinter.messagebox.showerror('Error','Category cannot be left empty.')
            else:
                self.con.add_category(self.create_ent.get())
                self.category()
                self.insert_category()
                self.reset_category()

    def add_password(self):
        if self.account_ent.get()=='' or self.category_ent.get()=='' or self.username_ent.get()=='' or \
                self.password_ent.get()=='':
            tkinter.messagebox.showerror('Error','Dont leave the fields empty.')
        else:
            self.con.add_password(self.account_ent.get(),self.category_ent.get(), self.username_ent.get(),
                               self.password_ent.get())
            self.insert_password()
            self.reset_password()

    def update_password(self):
        if self.account_ent.get() == '' or self.category_ent.get() == '' or self.username_ent.get() == '' or \
                self.password_ent.get() == '':
            tkinter.messagebox.showerror('Error', 'Dont leave the fields empty.')
        else:
            self.con.update_password(self.account_ent.get(), self.category_ent.get(), self.username_ent.get(),
                                  self.password_ent.get(), self.id)
            self.insert_password()
            self.reset_password()

    def delete_category(self):
        self.con.delete_category(self.create_ent.get())
        self.category()
        self.category_ent.set('')
        self.insert_category()
        self.insert_password()
        self.reset_category()

    def delete_password(self):
        self.con.delete_password(self.id)
        self.insert_password()
        self.reset_password()

    def reset_category(self):
        self.create_ent.delete(0, END)

    def reset_password(self):
        self.account_ent.delete(0, END)
        self.category_ent.set('')
        self.username_ent.delete(0, END)
        self.password_ent.delete(0, END)

    def insert_category(self):
        data = self.con.fetch_category()
        self.category_tbl.delete(*self.category_tbl.get_children())
        for i in data:
            self.category_tbl.insert("","end", value=(i[0]))
        self.category_tbl.bind('<Double-1>',self.select_category)

    def select_category(self, event):
        self.row = self.category_tbl.item(self.category_tbl.selection(), "values")
        self.fill_category()

    def fill_category(self):
        self.reset_category()
        self.create_ent.insert(0,self.row[0])

    def insert_password(self):
        data = self.con.fetch_password()
        self.password_tbl.delete(*self.password_tbl.get_children())
        for i in data:
            self.password_tbl.insert("","end", value=(i[1],i[2],i[3],i[4]), text=(i[0]))
        self.password_tbl.bind('<Double-1>',self.select_password)

    def select_password(self, event):
        self.row = self.password_tbl.item(self.password_tbl.selection(), "values")
        self.id = self.password_tbl.item(self.password_tbl.selection(), "text")
        self.fill_password()

    def fill_password(self):
        self.reset_password()
        self.account_ent.insert(0,self.row[0])
        self.category_ent.set(self.row[1])
        self.username_ent.insert(0,self.row[2])
        self.password_ent.insert(0,self.row[3])

    def category(self):
        data = self.con.fetch_category()
        self.category_ent['values'] = data

    def show(self):
        self.count += 1
        if self.count % 2 == 0:
            self.password_ent.configure(show="*")
        else:
            self.password_ent.configure(show='')

    def binary_search(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][0] == key:
                return mid
            elif list[mid][0] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1



