class Control:
    def __init__(self):
        self.__tv=TV

    def turnOn(self):
        self.__tv=TV.turnOn()

    def turnOff(self):
        self.__tv=TV.turnOff()

    def canalUp(self):
        self.__tv=TV.canalUp()

    def canalDown(self):
        self.__tv=TV.canalDown()

    def volumenUp(self):
        self.__tv=TV.volumenUp()

    def volumenDown(self):
        self.__tv=TV.volumenDown()

    def enlazar(self, tv:TV):
        self.__tv=tv
        self.__tv.set_Control(self)

    def set_Canal(self, canal: int):
        self.__tv.set_Canal(canal)

    def get_Tv(self):
        return self.__tv

    def set_Tv(self, tv: TV):
        self.__tv= tv        