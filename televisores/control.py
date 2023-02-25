class Control:
    def __init__(self):
        self._tv=None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def enlazar(self, tv):
        self.tv=tv
        self._tv.setControl(self)

    def set_Canal(self, canal: int):
        self._tv.setCanal(canal)

    def get_Tv(self):
        return self._tv

    def set_Tv(self, tv):
        self._tv= tv        