"""-----------------------------------------------------------------------------

Company     : Reutech Radar Systems
Name        : CXA_SSave
Designer    : jfolding
Generated   : 28/02/2019
--------------------------------------------------------------------------------
Description:
Screenshot saving module for Keysight CXA machines to be used with pyvisa

-----------------------------------------------------------------------------"""
import visa
import time
import os
from time import sleep

def saveScreenshot(instrument, fileLocation, fileName):
    # Connect to Instrument
    rm = visa.ResourceManager()
    suffx = ".PNG"
    image = (fileName+suffx)
    CXA = instrument
    saveLocation = (fileLocation+"/"+image)
    print(CXA,saveLocation)
    # Setup Block Data
    CXA.values_format.is_binary = True
    CXA.values_format.datatype = 'B'
    CXA.values_format.is_big_endian = False
    CXA.values_format.container = bytearray


    writeString = (":MMEM:STOR:SCR \"D:\{}\"").format(image)
    deleteString = (":MMEMory:DELete \"D:\{}\"").format(image)

    ##Save screenshot
    CXA.write(writeString)
    ##Copy block data to PC
    dname = (r"{}").format(saveLocation)
    fullname = (dname)
    ##print(dname)
    ##print(fullname)
    img = CXA.query_values('MMEM:DATA? \"D:\{}\"').format(image)
    sleep(0.5)
    target = open(dname, 'wb')
    target.write(img)
    target.close()
    print("{} saved.".format(saveLocation))

    ##Delete screenshot from ram
    CXA.write(deleteString)

    CXA.close()
    rm.close()

    # end of Untitled
