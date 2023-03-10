
class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.marca=marca
        self.canal=1
        self.precio=500
        self.estado=estado
        self.volumen=1
        self.control=None
        TV.numTV +=1

    def getNumTV():
        return TV.numTV
    def setNumTV(numTV):
        TV.numTV=numTV

    def turnOn(self):
        self.estado=True

    def turnOff(self):
        self.estado=False

    def getEstado(self):
        return self.estado

    def getMarca(self):
        return self.marca
    
    def setMarca(self,marca ):
        self.marca=marca   
    
    def getControl(self):
        return self.control
    
    def setControl(self,control):
        self.control=control
    
    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,precio):
        self.precio=precio

    def getVolumen(self):
        return self.volumen
    
    def setVolumen(self,volumen):
        if (self.estado==True):
            if (volumen >= 0 and volumen <=7):
                self.volumen=volumen
    
    def volumenUp(self):
        if (self.estado==True):
            if (self.volumen <7):
                self.volumen +=1
    
    def volumenDown(self):
        if (self.estado==True):
            if (self.volumen > 0):
                self.volumen -=1

    def getCanal(self):
        return self.canal
    
    def setCanal(self,canal):
        if (self.estado==True):
            if (canal >= 1 and canal <= 120):
                self.canal=canal

    def canalUp(self):
        if (self.estado==True):
            if ( self.canal < 120):
                self.canal +=1
    
    def canalDown(self):
        if (self.estado==True):
            if (self.canal > 1):
                self.canal -=1