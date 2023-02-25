
class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.__marca=marca
        self.__canal=1
        self.__precio=500
        self.__estado=bool
        self.__volumen=1
        self.__control=None
##################################################################
    def TV(self,marca,estado:bool):
        self.__marca=marca
        self.__estado=estado
        TV.numTV +=1

    @staticmethod
    def getNumTV():
        return TV.numTV
    @staticmethod
    def setNumTV(numTV:int):
        TV.numTV=numTV
################################################################
    def turnOn(self):
        self.__estado=True

    def turnOff(self):
        self.__estado=False

    def getEstado(self):
        return self.__estado
################################################################
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca ):
        self.__marca=marca   
    
    def getControl(self):
        return self.__control
    
    def setControl(self,control ):
        self.__control=control
    
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self,precio:int ):
        self.__precio=precio

##################################################################
    def getVolumen(self):
        return self.__volumen
    
    def set_Volumen(self,volumen:int ):
        self.__volumen=volumen
    
    def volumenUp(self):
        if (self.__estado==True):
            if (self.__volumen >= 0 and self.__volumen <7):
                self.__volumen +=1
    
    def volumenDown(self):
        if (self.__estado==True):
            if (self.__volumen > 0 and self.__volumen <= 7):
                self.__volumen -=1
###################################################################
    def getCanal(self):
        return self.__canal
    
    def setCanal(self,canal:int ):
        self.__canal=canal

    def canalUp(self):
        if (self.__estado==True):
            if (self.__canal >= 1 and self.__canal < 120):
                self.__canal +=1
    
    def canalDown(self):
        if (self.__estado==True):
            if (self.__canal > 1 and self.__canal <= 120):
                self.__canal -=1