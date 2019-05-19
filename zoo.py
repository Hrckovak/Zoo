from lekcia7.ZOO.pavilion import *
from lekcia7.ZOO.shop import *
from lekcia7.ZOO.animals1 import *

class Zoo:
    opening_hours = {
        "Monday - Friday": "11:00 - 17:00",
        "Saturday": "09:00 - 17:00",
        "Sunday": "Closed"
    }
    price_list = {"sezona": 12}
    entered = False

    def __init__(self, name, address, pavilions = None, shop = None):
        self.address = address
        self.name = name
        self.pavilions = pavilions
        self.shop = shop

    def show_opening_hours(self):
        ret = ""
        for key in self.opening_hours:
            ret +=f"{key:<20}\t{self.opening_hours[key]:>20}\n"
        return ret

    def change_opening_hours(self, key, value):
        self.opening_hours[key] = value

    def list_pavilions(self):
        """
        a)pavilon1
        b)pavilon2
        """
        ret = ""
        for idx, pavilion in enumerate (self.pavilions):
            ret += f"{idx:<5} {pavilion.name:<50}"
            return ret

    def add_pavilion(self, pavilion):
        if not isinstance(pavilion, Pavilion):
            return False
        if self.pavilions:
            self.pavilions.append(pavilion)
        else:
            self.pavilions = [pavilion]

    def remove_pavilion(self, name):
        if self.pavilions:
            for idx, pavilion in enumerate(self.pavilions):
                if pavilion.name == name:
                    del self.pavilions[idx]
# alebo self.pavilions.pop(idx)
        else:
# nic sa nezmazalo
            return False

    def add_shop(self, shop):
        if not isinstance(shop,Shop):
            return False
        if self.shop:
            self.shop.append(shop)
        else:
            self.shop = [shop]

    def enter(self):
        self.entered = True

    def feed (self):
        pass

    def pay_entry_fee (self):
        pass

if __name__== "__main__":
    meerkat = Meerkat ("Karol", "3", "M")
    meerkatf = Meerkat("Karolina", "3", "M")
    dingo1 = Dingo("Stefan", "12", "M")
    sand1 = Pavilion("Sand", "sand1", [meerkat, meerkatf])
    Zoo = Zoo("Zoo1", "Einsteinova,Bratislava", [sand1])
    sand1.add_animal(dingo1)
    for animal in Zoo.pavilions[0].animals:
        print(animal.name)
    print(Zoo.list_pavilions())


"Co chces robit:"\
"1) Zobraz otvaracie hodiny"\
"2) Zobraz pavilony"\
"3) Zobraz obchody"\
"4) Zobraz ponuku obchodu <meno>"\