"""
A simple program that stores book information:
Title, Author, Year, ISBN

User can :
View all records,
Search an entry,
Add entry,
Update entry,
Delete,
Close
"""

from tkinter import *
import back_end

def get_selected_row(event):
    global selected_tuple
    index=list_space.curselection()[0]
    selected_tuple=list_space.get(index)
    entry_title.delete(0,END)
    entry_title.insert(END, selected_tuple[1])
    entry_author.delete(0,END)
    entry_author.insert(END, selected_tuple[2])
    entry_year.delete(0,END)
    entry_year.insert(END, selected_tuple[3])
    entry_isbn.delete(0,END)
    entry_isbn.insert(END, selected_tuple[4])

def view_command():
    list_space.delete(0,END)
    for item in back_end.view():
        list_space.insert(END, item)

def search_command():
    list_space.delete(0,END)
    for search_item in back_end.search(title_text.get(), entry_author.get(), entry_year.get(), entry_isbn.get()):
        list_space.insert(END, search_item)


def insert_command():
    back_end.insert(title_text.get(), entry_author.get(), entry_year.get(), entry_isbn.get())
    list_space.delete(0,END)
    list_space.insert(END, (title_text.get(), entry_author.get(), entry_year.get(), entry_isbn.get()))

def delete_command():
    back_end.delete(selected_tuple[0])

def update_command():
    back_end.update(selected_tuple[0], title_text.get(), entry_author.get(), entry_year.get(), entry_isbn.get())
    
    list_space.delete(0,END)
    list_space.insert(END, (title_text.get(), entry_author.get(), entry_year.get(), entry_isbn.get()))






window=Tk()

window.wm_title("Bookstore")

title_label=Label(window, text="Title")
title_label.grid(row=0,column=0)

author_label=Label(window, text="Author")
author_label.grid(row=0,column=2)

year_label=Label(window, text="Year")
year_label.grid(row=1,column=0)

isbn_label=Label(window, text="ISBN")
isbn_label.grid(row=1,column=2)

title_text=StringVar()
entry_title=Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

author_text=StringVar()
entry_author=Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

year_text=StringVar()
entry_year=Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

isbn_text=StringVar()
entry_isbn=Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)

list_space=Listbox(window, height=6, width=35)
list_space.grid(row=2, column=0, rowspan=6, columnspan=2)

list_space.bind('<<ListboxSelect>>', get_selected_row)

scroll=Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

list_space.configure(yscrollcommand=scroll.set)
scroll.configure(command=list_space)

view_button=Button(window, text="View all", width=12,command=view_command)
view_button.grid(row=2, column=3)

search_button=Button(window, text="Search Entry", width=12,command=search_command)
search_button.grid(row=3, column=3)

add_button=Button(window, text="Add Entry", width=12, command=insert_command)
add_button.grid(row=4, column=3)

update_button=Button(window, text="Update Entry", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button=Button(window, text="Delete", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button=Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)



window.mainloop()
