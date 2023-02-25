class Control:
    def __init__(self):
        self.tv=None

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def enlazar(self, tv):
        self.tv=tv
        self.tv.setControl(self)

    def set_Canal(self, canal: int):
        self.tv.setCanal(canal)

    def get_Tv(self):
        return self.tv

    def set_Tv(self, tv):
        self.tv= tv        