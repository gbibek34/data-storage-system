from tkinter import *
from tkinter import ttk
from tkinter import Menu
from Password import PasswordManager
from Notes import NotesManager
from Contacts import ContactManager
from Options import Options

class Notebook:
    def __init__(self, window):
        self.wn = window
        self.wn.title("Registry")
        self.wn.geometry("1265x545+200+100")
        self.tabs = ttk.Notebook(window)
        self.notes = Frame(self.tabs)
        self.contacts = Frame(self.tabs)
        self.password = Frame(self.tabs)
        self.options = Frame(self.tabs)
        self.tabs.add(self.notes, text="Notes")
        self.tabs.add(self.contacts, text="Contacts")
        self.tabs.add(self.password, text="Passwords")
        self.tabs.add(self.options, text="Options")
        self.tabs.pack(expand=1, fill='both')
        NotesManager(self.notes)
        ContactManager(self.contacts)
        PasswordManager(self.password)
        Options(self.options, self.wn)

if __name__ == '__main__':
    window = Tk()
    Notebook(window)
    window.mainloop()