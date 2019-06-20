try:
    from tkinter import *
    from tkinter import ttk
    from tkinter.messagebox import *
    import tkinter as tk
    from tkinter.filedialog import askdirectory
except:
    from Tkinter import *
    import ttk
    import tkMessageBox
    # from tkinter.messagebox import *
    import Tkinter as tk
    # from tkinter.filedialog import askdirectory
    from tkFileDialog import askdirectory



from instListModule import *
from CXA_SSave import * #screenshot module for specific machine
import os

root = tk.Tk()
root.title("File Save UI")
#Create Tabbed Interface
#Create Notebook and tabs
tab_control = ttk.Notebook(root)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Save Screenshot')
tab_control.add(tab2, text='Instrument Setup')
#page = ilc.instList(tab2)
createInstList(tab2)



defaultName = None
saveLocation = None
fileFormat = ["BMP", "JPEG"]


def saveButton():

    if e1.index("end") == 0:
        print("Please choose a save directory!")
    elif e2.index("end") == 0:
        print("Please add file name!")
    else:

        frmt = str(fileFormat[picFormat.get()])
        #fullname =str((e1.get() + "/" + e2.get()))
        fullname = (e1.get()+"/"+ e2.get()+"."+frmt)
        if os.path.exists(fullname):
            print("File exists")
            if askyesno('Overwrite?', 'This file already exists. Do you want to overwrite?'):
                showwarning('Warning', '%s will be overwritten' % fullname)
                saveFile(fullname, frmt)

            else:
                showinfo('Rename File', 'Please enter a new file name')
        else:
            inst = getInst()
            instrument = vi.Instrument(inst)
            print(instrument.realname)
            saveScreenshot(instrument.realname,e1.get(),e2.get())
            #print(fullname)
            #print(frmt)


def openDialog():
    defaultName= askdirectory()
    e1.delete(0, END)
    e1.insert(0, defaultName)
    print(defaultName)
    return


#Setup Frames
tab_control.pack(expand=1, fill='both')
f1 = tk.Frame(tab1, width=400, height=180)
f2 = tk.Frame(f1, width=300, height=250)
f3 = tk.Frame(f1, width=200, height=50)
f4 = tk.Frame(f3, width=300, height=100)
f5 = tk.Frame(f1, width=200, height=10)
#f6 = tk.Frame(f1, width=200, height=10)
#f7 = tk.Frame(f1, width=200, height=10)
separator1 = Frame(f1, height=2, bd=1, relief=SUNKEN)
separator2 = Frame(f1, height=2, bd=1, relief=SUNKEN)
#pack the frames
f1.pack(expand=1)
f1.pack_propagate(0) #fix size
f2.pack()
separator1.pack(fill=X, padx=5, pady=5)
f3.pack(fill=X)
f4.pack(side=TOP, expand=FALSE)
separator2.pack(fill=X, padx=5, pady=5)
f5.pack(side=TOP, fill=X)




#Text entry
e1 = Entry(f2, width = 50)
e2 = Entry(f2, width = 50)
e2.focus_set() #put cursor in first box
e1.grid(row=2, column=1, padx=5, pady=3,)
e2.grid(row=4, column=1, padx=5, pady=3)

#e1.insert(10,defaultName)
#e2.insert(10,"Enter File Name...")

#Labels
label1 = Label(f2,text="Select Save Location..")
label1.grid(row=1,column=1, sticky = W)
label2 = Label(f2,text="Enter File Name..")
label2.grid(row=3,column=1, sticky = W)


#Buttons
button = Button(f2, text = "Open Folder", padx=5, pady=1, width=9, command=openDialog).grid(row=2, column = 2)
button = Button(f2, text = "Save File", padx=5, pady=1, width=9, command=saveButton).grid(row=4, column = 2)
#button = Button(f4, text = "Save", padx=5, pady=3, width=7).pack(side=LEFT, fill=X)
button = Button(f5, text = "Quit", padx=5, pady=1, width=9, command=quit).pack(side=TOP)

#Radio buttons
picFormat = tk.IntVar()
picFormat.set(0)


tk.Radiobutton(f4,text=".BMP", variable=picFormat, value=0).grid(row=1, column=1)
tk.Radiobutton(f4,text=".JPEG", variable=picFormat, value=1, state=DISABLED).grid(row=1, column=2)


#add names

#Main
inst = getInst()
print(inst)
mainloop()
