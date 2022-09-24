from tkinter import *
from backend import Database

path = "books.db"

database = Database(path)

class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Book Store")

        bgcolor = 'black'
        fontcolor = 'white'

        self.window['bg'] = bgcolor
        
        # Labels

        l1 = Label(window, text = "Title")
        l1['bg'] = bgcolor
        l1['fg'] = fontcolor
        l1.grid(row = 0, column = 0, padx = 2, pady = 5)

        l2 = Label(window, text = "Author")
        l2['bg'] = bgcolor
        l2['fg'] = fontcolor
        l2.grid(row = 0, column = 2, padx = 2, pady = 5)

        l3 = Label(window, text = "Year")
        l3['bg'] = bgcolor
        l3['fg'] = fontcolor
        l3.grid(row = 1, column = 0, padx = 2, pady = 5)

        l4 = Label(window, text = "ISBN")
        l4['bg'] = bgcolor
        l4['fg'] = fontcolor
        l4.grid(row = 1, column = 2, padx = 2, pady = 5)

        # Entries

        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable = self.title_text)
        self.e1.grid(row = 0, column = 1, padx = 2, pady = 5)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable = self.author_text)
        self.e2.grid(row = 0, column = 3, padx = 2, pady = 5)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable = self.year_text)
        self.e3.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable = self.isbn_text)
        self.e4.grid(row = 1, column = 3, padx = 5, pady = 5)

        # List

        self.list1 = Listbox(window, height = 10, width = 35)
        self.list1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2, padx = 5)

        self.sb1 = Scrollbar(window)
        self.sb1.grid(row = 2, column = 2, rowspan = 6)

        self.list1.configure(yscrollcommand = self.sb1.set)
        self.sb1.configure(command = self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # Buttons

        b1 = Button(window, text = "View all", width = 12, command = self.view_command)
        b1.grid(row = 2, column = 3, pady = 2)

        b2 = Button(window, text = "Search entry", width = 12, command = self.search_command)
        b2.grid(row = 3, column = 3, pady = 2)

        b3 = Button(window, text = "Add entry", width = 12, command = self.add_command)
        b3.grid(row = 4, column = 3, pady = 2)

        b4 = Button(window, text = "Update selected", width = 12, command = self.update_command)
        b4.grid(row = 5, column = 3, pady = 2)

        b5 = Button(window, text = "Delete", width = 12, command = self.delete_command)
        b5.grid(row = 6, column = 3, pady = 2)

        b6 = Button(window, text = "Close", width = 12, command = window.destroy)
        b6.grid(row = 7, column = 3, pady = 2)

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.list1.curselection()[0]
            selected_tuple = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_command(self):
        database.delete(selected_tuple[0])
        self.view_command()

    def update_command(self):
        database.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()

window = Tk()
Window(window)
window.mainloop()

