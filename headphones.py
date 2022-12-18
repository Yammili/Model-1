class Headphones():
    def __init__(self, brand, model, fit, color):
        self.brand = brand
        self.model = model
        self.fit = fit
        self.color = color

    def info(self):
        print("\nCompany: %s \nModel: %s \nColor: %s \nFit: %s" %(
            self.brand.title(), self.model.title(), self.fit.title(), 
            self.color.title())
        )


class CorpsOnHead():
    def __init__(self):
        self.corps = input("Corps: ")
        self.ear_pads = input("Ear pads: ")
        self.cups = input("Cups: ")

    def info(self):
        return("Corps: %s \nEar pads: %s \nCups: %s" %(
            self.corps.title(), self.ear_pads.title(), self.cups.title())
        )


class CorpsInEar():
    def __init__(self):
        self.corps = input("Corps: ")
        self.size = input("Size: ")

    def info(self):
        return("Corps: %s \nSize: %s" %(self.corps.title(), self.size.title()))


class Wired(Headphones):
    def __init__(self, brand, model, fit, color, type_connection, cord_length):
        super().__init__(brand, model, fit, color)
        self.type_connection = type_connection
        self.cord_length = cord_length
        if self.fit.title() == "Onhead":
            self.detail = CorpsOnHead()
        else:
            self.detail = CorpsInEar()

    def all_info(self):
        super().info()
        print(self.detail.info(), "\nType connection: %s \nCord length: %s m\n" %(
            self.type_connection.title(), self.cord_length) 
            )


class Wireless(Headphones):
    def __init__(self, brand, model, fit, color, wireless, autonomy):
        super().__init__(brand, model, fit, color,)
        self.wireless = wireless
        self.autonomy = autonomy
        if self.fit.title() == "Onhead":
            self.detail = CorpsOnHead()
        else:
            self.detail = CorpsInEar()
        
    def all_info(self):
        super().info() 
        print(self.detail.info(), "\nWireless: %s \nAutonomy: %s hours\n" %(
            self.wireless.title(), self.autonomy)
        )