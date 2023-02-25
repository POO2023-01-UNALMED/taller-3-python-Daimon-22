class TV:
    numTV=0
    def __init__(self):
        self.__marca=Marca
        self.__canal=1
        self.__precio=500
        self.__estado
        self.__volumen=1
        self.__control=Control
##################################################################
    def TV(self,marca:Marca,estado:bool()):
        self.__marca=marca
        self.__estado=estado
        TV.numTV +=1

    @staticmethod
    def get_NumTV():
        return TV.numTV
    @staticmethod
    def set_NumTV(numTV:int):
        TV.numTV=numTV
################################################################
    def turnOn(self):
        self.__estado=True

    def turnOff(self):
        self.__estado=False

    def get_Estado(self):
        return self.__estado
################################################################
    def get_Marca(self):
        return self.__marca
    
    def set_Marca(self,marca:Marca ):
        self.__marca=marca   
    
    def get_Control(self):
        return self.__control
    
    def set_Control(self,control:Control ):
        self.__control=control
    
    def get_Precio(self):
        return self.__precio
    
    def set_Precio(self,precio:int ):
        self.__precio=precio

##################################################################
    def get_Volumen(self):
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
    def get_Canal(self):
        return self.__canal
    
    def set_Canal(self,canal:int ):
        self.__canal=canal

    def canalUp(self):
        if (self.__estado==True):
            if (self.__canal >= 1 and self.__canal < 120):
                self.__canal +=1
    
    def canalDown(self):
        if (self.__estado==True):
            if (self.__canal > 1 and self.__canal <= 120):
                self.__canal -=1