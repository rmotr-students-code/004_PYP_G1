class Car(object):

    def __init__(self):
        pass

    def start_engine(self):
        print("Starting engine...")

    def spin_wheels(self):
        print("Spinning 2 wheels...")

    def change_gear(self):
        print("Changing gear...")

    def drive(self):
        self.start_engine()
        self.change_gear()
        self.spin_wheels()


class ConvertibleMixin(object):

    def open_roof(self):
        print("Opening car's roof...")


class FourWheelDriveMixin(object):

    def spin_wheels(self):
        print("Spinning 4 wheels...")


class AutomaticTransmissionMixin(object):

    def drive(self):
        self.start_engine()
        self.spin_wheels()


class Porsche911Cabriolet(ConvertibleMixin, Car):
    """Convertible, 2-wheels drive, manual transmission car"""
    pass


class SubaruImpreza(FourWheelDriveMixin, AutomaticTransmissionMixin, Car):
    """4-wheels drive, automatic transmission car"""
    pass


class ChrevroletCamaro(ConvertibleMixin, AutomaticTransmissionMixin, Car):
    pass


p = Porsche911Cabriolet()
p.open_roof()
p.drive()

s = SubaruImpreza()
s.drive()