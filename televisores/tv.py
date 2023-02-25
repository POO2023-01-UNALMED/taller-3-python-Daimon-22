
class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.marca=marca
        self.canal=1
        self.precio=500
        self.estado=bool
        self.volumen=1
        self.control=None
##################################################################
    def TV(self,marca,estado:bool):
        self.marca=marca
        self.estado=estado
        TV.numTV +=1

    @staticmethod
    def getNumTV():
        return TV.numTV
    @staticmethod
    def setNumTV(numTV:int):
        TV.numTV=numTV
################################################################
    def turnOn(self):
        self.estado=True

    def turnOff(self):
        self.estado=False

    def getEstado(self):
        return self.estado
################################################################
    def getMarca(self):
        return self.marca
    
    def setMarca(self,marca ):
        self.marca=marca   
    
    def getControl(self):
        return self.control
    
    def setControl(self,control ):
        self.control=control
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,precio:int ):
        self.precio=precio

##################################################################
    def getVolumen(self):
        return self.volumen
    
    def set_Volumen(self,volumen:int ):
        self.volumen=volumen
    
    def volumenUp(self):
        if (self.estado==True):
            if (self.volumen >= 0 and self.volumen <7):
                self.volumen +=1
    
    def volumenDown(self):
        if (self.estado==True):
            if (self.volumen > 0 and self.volumen <= 7):
                self.volumen -=1
###################################################################
    def getCanal(self):
        return self.canal
    
    def setCanal(self,canal:int ):
        self.canal=canal

    def canalUp(self):
        if (self.estado==True):
            if (self.canal >= 1 and self.canal < 120):
                self.canal +=1
    
    def canalDown(self):
        if (self.estado==True):
            if (self.canal > 1 and self.canal <= 120):
                self.canal -=1