import pyodbc as pyodbc
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from isbnlib import canonical, meta

global title
global auth_string
global publisher
global year
global providers
global db_str


class Library(tk.Tk):
    def __init__(self):
        super().__init__()
        global providers
        global db_str
        self.title('Add to the Library')
        self.geometry("200x100")

        self.isbn_ent = Entry(self, width=20)
        self.isbn_ent.pack(padx=10, pady=20)

        submit_btn = Button(self, text="Submit", command=self.submit)
        submit_btn.pack()

        providers = ['goob', 'openl', 'wikidata', 'worldcat']
        db_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ={YOUR_PATH_HERE}\Library.accdb')

    def run_isbn(self):
        global title
        global auth_string
        global publisher
        global year
        isbn = canonical(self.isbn_ent.get())
        book = None

        for provider in providers:
            try:
                book = meta(isbn, service=provider)
            except:
                pass

        if book:
            title = book['Title']
            authors = book['Authors']
            year = book['Year']
            publisher = book['Publisher']
            auth_string = ', '.join(authors)

        else:
            title = "Not found"
            author = "Not found"
            year = "Not found"
            publisher = "Not found"

    def submit(self):
        self.run_isbn()
        print(title)
        print(auth_string)
        print(year)
        print(publisher)


        sqlSubmit = ("""INSERT INTO Library (TITLE, AUTHOR, YEAR_PUBLISHED, PUBLISHER) VALUES ( """
                     + chr(39) + title + chr(39) + ', ' + chr(39) + auth_string + chr(
                    39) + ', ' + chr(39) + year + chr(39) + ', ' + chr(39) + publisher + chr(39) + ')')

        libConn = pyodbc.connect(db_str)
        libCur = libConn.cursor()

        libCur.execute(sqlSubmit)

        libConn.commit()
        libConn.close()

        messagebox.showinfo("Done!", f"{title} has been added to the Library!")


if __name__ == "__main__":
    lib = Library()
    lib.mainloop()
