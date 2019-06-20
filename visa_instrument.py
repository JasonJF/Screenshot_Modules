#---------------------------------------------------------------------------------------------------------------------
# Name          : instListClass
# Creator       : Jason Folding
# Date          : 26/02/19
# Description   : A class to create visa instruments
#-------------------------------------------------------------------------------------------------------------------

import visa

class InstrumentList():
    def __init__(self):
        rm = visa.ResourceManager()
        self.instruments = rm.list_resources()

class Instrument():

    def __init__(self, address):
        rm = visa.ResourceManager()
        #self.instruments = rm.list_resources()
        self.address = address
        self.realname = rm.open_resource(self.address)
        self.name = self.realname.query('*IDN?')



    def getID(self):
        print(self.name)
        resp = self.name
        return resp

    def sendRead(self):
        resp=(self.realname.read())
        return resp

    def sendCommand(self, command):
        cmd = command
        self.realname.write(cmd)
    def sendQuery(self,command):
        cmd = command
        resp =(self.realname.query(cmd))
        return resp