class Cat:
    def __init__(self,color=None,num_of_leg=None,kind=None):
        self.color = color
        self.num_of_leg=num_of_leg
        self.__kind = kind
    
    def show_identity(self):
        print(f'saya kucing dengan detail, Warna Bulu: {self.color} dengan jumlah kaki : {self.num_of_leg} dan kucing jenis {self.__kind}')
    
    def tingkah_laku(self):
        if self.__kind == 'Kampung':
            print("Kucing bar bar")
        elif self.__kind == 'Angora':
            print("Kucing kalem")
        else :
            print("Tingkah laku belum diteliti")

Garong = Cat('Hitam',4,'Kampung')
Felixiana = Cat('Emas',4,'Angora')
Garong.show_identity()
Garong.tingkah_laku()
Felixiana.show_identity()
Felixiana.tingkah_laku()

class Fish:
    def __init__(self,types=None,feed=None):
        self.type = types
        self.feed = feed
    
    def show_identity(self):
        print(f'saya Ikan dengan detail, Jenis: {self.type}, makanan: {self.feed}')

paus = Fish("paus","plankton")
cupang = Fish("cupang","cacing")
arwana = Fish("arwana","jangkrik")
sapu_sapu = Fish("sapu-sapu","pelet")
paus.show_identity()
cupang.show_identity()
arwana.show_identity()
sapu_sapu.show_identity()

class Flower:
    def __init__(self,nama=None,color=None,num_of_petal=None):
        self.color = color
        self.nama = nama
        self.num_of_petal = num_of_petal

    def show_identity(self):
        print(f'saya Bunga dengan detail, Jenis: {self.nama}, color: {self.color}, num of petal: {self.num_of_petal}')

bangkai = Flower('bangkai','merah',12)
anggrek = Flower('anggrek','putih',8)
mawar = Flower('mawar','merah',3)
melati = Flower('melati','kuning',5)
bangkai.show_identity()
anggrek.show_identity()
mawar.show_identity()
melati.show_identity()

class Car:
    def __init__(self,types=None,color=None,num_of_tire=None):
        self.type = types
        self.color = color
        self.num_of_tire = num_of_tire
    
    def show_identity(self):
        print(f'saya mobil dengan detail, Type: {self.type}, color: {self.color}, num of tire: {self.num_of_tire}')

sedan = Car('sedan','merah',4)
truk = Car('truk','hijau',6)
tronton = Car('tronton','coklat',12)
angkot = Car('angkot','kuning',4)
sedan.show_identity()
truk.show_identity()
tronton.show_identity()
angkot.show_identity()










        