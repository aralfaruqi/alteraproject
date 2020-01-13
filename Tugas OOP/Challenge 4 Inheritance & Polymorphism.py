class Animal:
    def __init__(self,nama,jenis=None,gigi=None):
        self.nama = nama
        self.jenis = jenis
        self.gigi = gigi
    
    types = "Parent of All Animal"
    def identify_myself(self):
        return f"Hi I'm {self.types}, My Name is {self.nama}"
    
class Herbivor(Animal):
    def __init__(self,nama,jenis=None,gigi=None):
        super().__init__(nama,jenis="'tumbuhan'",gigi="tumpul")
    
    types="Herbivor "
    def identify_myself(self):
        return super().identify_myself() + f", My Food is {self.jenis}, I have {self.gigi} teeth"

class Carnivor(Animal):
    def __init__(self,nama,jenis=None,gigi=None):
        super().__init__(nama,jenis="'daging'",gigi="tajam")
    
    types="Carnivor "
    def identify_myself(self):
        return super().identify_myself() + f", My Food is {self.jenis}, I have {self.gigi} teeth"

class Omnivor(Animal):
    def __init__(self,nama,jenis=None,gigi=None):
        super().__init__(nama,jenis="'semua'",gigi="tumpul")
    
    types="Omnivor "
    def identify_myself(self):
        return super().identify_myself() + f", My Food is {self.jenis}, I have {self.gigi} teeth"

Binatang = Animal('Binatang')
Kambing = Herbivor('Kambing')
Singa = Carnivor('Singa')
Ayam = Omnivor('Ayam')
print(Binatang.identify_myself())
print(Kambing.identify_myself())
print(Singa.identify_myself())
print(Ayam.identify_myself())


