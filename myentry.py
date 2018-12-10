# importing the tkinter module which allows you to make windows
from tkinter import*
# Tk() makes a window. This assigns master to Tk()
master=Tk()
master2=Tk()

def return_entry(en):
    """Gets and prints the content of the entry"""
    content=int(entry.get())
    print(content)
    content2=int(entry2.get())
    print(content2)    
    print(content*content2)


    
Label(master, text="Input: ").grid(row=0, sticky =W)

#entry is the box that you type something in
entry =Entry(master)
entry2=Entry(master2)
#this is where the entry box is
entry.grid(row=0,column=1)
entry2.grid(row=0,column=1)

#this means that when you click enter/return, it
entry.bind('<Return>', return_entry)
entry2.bind('<Return>', return_entry)


#loops the program which keeps the window open
mainloop()