#load different tkinter versions for Python 2.7 or Python 3.X
try:
    from tkinter import *
except:
    from Tkinter import *

import visa
#from tkinter import *
import visa_instrument as vi

global root

if __name__ == "__main__":
    root = Tk()
    tkvar = StringVar(root)
else:
    print("This is a module")
    #createInstList()

#------------------------------------------------------------------------------------------------------------------
#Variables

# instrumentList = {}                         #list of instruments
# rm = visa.ResourceManager()                 #resource manager
instList = vi.InstrumentList() #list of instrument addresses
instruments = instList.instruments
inst = ""  # rm.open_resource(tkvar.get())  #item in instruments
# print(type(instruments))
name = ""
address = ""
realname = []
tempname = []
#result = ""
#------------------------------------------------------------------------------------------------------------------
#Class Code



def createInstList(tab):
    root = tab
    global tkvar
    tkvar = StringVar(root)
    # import tkinter as ttk
    # from ttk import *
    # instruments = []






    # ##IDN Loop
    # for instrument in instruments:#[1:]:  # skip first line
    #
    #     # print(instrument)
    #     address = rm.open_resource(instrument)
    #     # name = address.query('*IDN?')
    #     realname.append(name)
    #     instrumentList[instrument] = name
    #     # print(instrumentList)
    #
    # print(instrumentList)

    # IDN command
    def id_call():
        ##send idn
        inst = (tkvar.get())
        tempInst = vi.Instrument(inst)
        instName =(tempInst.getID())
        idLabel.configure(text=instName)


        # #sendQueryCommand('*IDN?')
        # instName = inst.query('*IDN?')





    # add a grid
    mainframe = Frame(root)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    mainframe.pack(pady=10, padx=10)

    # create tkinter variable
    instName = ""

    # Dictionary with options


    tkvar.set(instruments[1])  # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *instruments)
    popupMenu.configure(width=35)
    Label(mainframe, text="Choose an instrument").grid(row=1, column=1)
    popupMenu.grid(row=2, column=1)
    # IDN button
    Button(mainframe, text="*IDN?", command=id_call).grid(row=3, column=1)
    idLabel = Label(mainframe, text="instrument", fg='green')
    idLabel.grid(row=4, column=1)

    # on change dropdown value
    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)

def getInst():
    inst = (tkvar.get())
    return inst


