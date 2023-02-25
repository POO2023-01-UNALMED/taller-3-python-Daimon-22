class Control:
    def __init__(self):
        self.__tv=None

    def turnOn(self):
        self.__tv.turnOn()

    def turnOff(self):
        self.__tv.turnOff()

    def canalUp(self):
        self.__tv.canalUp()

    def canalDown(self):
        self.__tv.canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()

    def volumenDown(self):
        self.__tv.volumenDown()

    def enlazar(self, tv):
        self.__tv=tv
        self.__tv.setControl(self)

    def set_Canal(self, canal: int):
        self.__tv.setCanal(canal)

    def get_Tv(self):
        return self.__tv

    def set_Tv(self, tv):
        self.__tv= tv        