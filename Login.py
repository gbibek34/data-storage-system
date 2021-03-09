from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
import Notebook
from Queries import Queries
import os
os.chdir(r"E:\Assignment\Sem 2\Algorithm\Data Storage System")

class Login:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Login")
        self.wn.geometry("400x500+600+100")
        self.con = Queries()
        #Images
        self.login_img = ImageTk.PhotoImage(Image.open("Icons\Login.png").resize((100, 100)))
        #Frames
        self.frame1 = Frame(self.wn, relief=GROOVE, bd=5)
        self.frame1.place(x=10,y=10, height=480, width=380)
        #Lables
        self.login_image = Label(self.frame1, image=self.login_img)
        self.login_image.place(x=140, y=20)
        self.login_lbl = Label(self.frame1, text="Login", font=('verdana', 15))
        self.login_lbl.place(x=165, y=120)
        self.uname_lbl = Label(self.frame1, text="Username :", font=('verdana', 15))
        self.uname_lbl.place(x=10, y=180)
        self.pass_lbl = Label(self.frame1, text="Password :", font=('verdana', 15))
        self.pass_lbl.place(x=10, y=230)
        #Entries
        self.uname_ent = Entry(self.frame1, font=('arial', 15), width=18)
        self.uname_ent.place(x=150, y=180)
        self.pass_ent = Entry(self.frame1, font=('arial', 15), width=18, show='*')
        self.pass_ent.place(x=150, y=230)
        #Buttons
        self.login_btn = Button(self.frame1, text="Login", font=('arial', 15), width=10, command=self.login)
        self.login_btn.place(x=50, y=300)
        self.register_btn = Button(self.frame1, text="Reset", font=('arial', 15), width=10, command=self.reset)
        self.register_btn.place(x=200, y=300)
        self.register_btn = Button(self.frame1, text="Register", font=('arial', 15), width=10, command=self.register)
        self.register_btn.place(x=130, y=360)
#Methods
    def login(self):
        data = self.con.fetch_user()
        for i, j in data:
            if i == self.uname_ent.get() and j == self.pass_ent.get():
                tkinter.messagebox.showinfo('Success', 'Welcome to Data Storage System.')
                self.wn.withdraw()
                self.login = Toplevel(self.wn)
                Notebook.Notebook(self.login)
                return
        else:
            tkinter.messagebox.showerror('Login Failed', 'Invalid Username or Password')

    def reset(self):
        self.uname_ent.delete(0, END)
        self.pass_ent.delete(0, END)

    def register(self):
        self.wn.withdraw()
        self.login = Toplevel(self.wn)
        Register(self.login)



class Register:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Register")
        self.wn.geometry("500x500+600+100")
        self.con = Queries()
        #Images
        self.lbl = Label(self.wn, text="test")
        self.lbl.place(x=10, y=10)
        self.reg_image = ImageTk.PhotoImage(Image.open("Icons\Register.png").resize((100, 100)))
        #Frames
        self.frame1 = Frame(self.wn, relief=GROOVE, bd=5)
        self.frame1.place(x=10,y=10, height=480, width=480)
        # Lables
        self.reg_img = Label(self.wn, image=self.reg_image)
        self.reg_img.place(x=200, y=20)
        self.register_lbl = Label(self.frame1, text="Register", font=('verdana', 15))
        self.register_lbl.place(x=190, y=120)
        self.uname_lbl = Label(self.frame1, text="Username :", font=('verdana', 15))
        self.uname_lbl.place(x=20, y=180)
        self.email_lbl = Label(self.frame1, text="E-Mail :", font=('verdana', 15))
        self.email_lbl.place(x=20, y=240)
        self.cpass_lbl = Label(self.frame1, text="Password :", font=('verdana', 15))
        self.cpass_lbl.place(x=20, y=300)
        #Entries
        self.uname_ent = Entry(self.frame1, font=('verdana', 15))
        self.uname_ent.place(x=160, y=180)
        self.email_ent = Entry(self.frame1, font=('verdana', 15))
        self.email_ent.place(x=160, y=240)
        self.pass_ent = Entry(self.frame1, font=('verdana', 15), show='*')
        self.pass_ent.place(x=160, y=300)
        #Buttons
        self.reg_btn = Button(self.frame1, text="Register", font=('arial', 15), width=10, command=self.register_user)
        self.reg_btn.place(x=100, y=360)
        self.reset_btn = Button(self.frame1, text="Reset", font=('arial', 15), width=10, command=self.reset)
        self.reset_btn.place(x=260, y=360)
        self.login_btn = Button(self.frame1, text="Login", font=('arial', 15), width=10, command=self.login)
        self.login_btn.place(x=180, y=420)
#Methods
    def register_user(self):
        data = self.con.fetch_user()
        username = self.uname_ent.get()
        result = self.binary_search(data, username)
        if result != -1:
            tkinter.messagebox.showerror('Error', 'Username already exists')
        else:
            if self.uname_ent.get() == '' or self.email_ent.get() == '' or self.pass_ent.get() == '':
                tkinter.messagebox.showerror('Error', 'Dont leave the fields empty.')
            else:
                self.con.add_user(self.uname_ent.get(), self.email_ent.get(), self.pass_ent.get())
                tkinter.messagebox.showinfo('Success', 'User registered sucessfully')
                self.reset()

    def reset(self):
        self.uname_ent.delete(0, END)
        self.email_ent.delete(0, END)
        self.pass_ent.delete(0, END)

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

    def login(self):
        self.wn.withdraw()
        self.login = Toplevel(self.wn)
        Login(self.login)

if __name__ == '__main__':
    window = Tk()
    Login(window)
    window.mainloop()