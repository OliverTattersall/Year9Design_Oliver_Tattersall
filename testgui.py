from tkinter import *
master = Tk()
master.config(background="orange")
label=Label(master, text="Hockey Pool")
label.config(foreground="black")
label.pack()
button=Button(master, text="Quit", fg ="red", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(background="orange")
listbox.config(fg="black")
listbox.pack()
listbox.insert(END, "Player, Goals")
lst = [["connor mcdavid", 208],["sidney", 234],["steven stamkos", 187], ["austen matthews",70]]
for item in lst:
    listbox.insert(END, item[0]+"_"+str(item[1]))
    
mainloop()