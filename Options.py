from tkinter import *
from PIL import ImageTk, Image

class Options:
    def __init__(self, options, window):
        self.options = options
        self.window= window
        #Images
        self.logout_image = ImageTk.PhotoImage(Image.open("Icons/Logout.png").resize((200, 200)))
        self.exit_image = ImageTk.PhotoImage(Image.open("Icons/Exit.png").resize((200, 200)))
        #Frames
        self.frame1 = Frame (self.options, relief=RIDGE, bd=5)
        self.frame1.place(x=10, y=10, height=500, width=1240)
        #Labels
        self.logout_lbl = Label(self.frame1, text='Logout', font=('verdana', 20))
        self.logout_lbl.place(x=350, y=350)
        self.exit_lbl = Label(self.frame1, text='Exit', font=('verdana', 20))
        self.exit_lbl.place(x=780, y=350)
        #Buttons
        self.logout_btn = Button(self.frame1, image=self.logout_image, command=self.logout)
        self.logout_btn.image = self.logout_image
        self.logout_btn.place(x=300, y=100)
        self.exit_btn = Button(self.frame1, image=self.exit_image, command=self.exit)
        self.exit_btn.image = self.exit_image
        self.exit_btn.place(x=700, y=100)
#Method
    def logout(self):
        import Login
        self.window.withdraw()
        self.logout = Toplevel(self.window)
        Login.Login(self.logout)

    def exit(self):
        self.window.destroy()

