import random

class Kandang:
    def kambing(self):
        return "|||"+"\n"+"|"+self.OKBLUE+"K"+self.ENDC+"|"+"\n"+"|||"+"\n"+"\n"
    
    def bebek(self):
        return "|||"+"\n"+"|"+self.OKYELLOW+"B"+self.ENDC+"|"+"\n"+"|||"+"\n"+"\n"

    def zebra(self):
        return "|||"+"\n"+"|"+self.OKRED+"Z"+self.ENDC+"|"+"\n"+"|||"+"\n"+"\n"

    def nomor(self,number):
        return "|||"+"\n"+f"|{number}|"+"\n"+"|||"+"\n"+"\n"

class Board(Kandang):
    list_hewan = ["K","Z","B"]
    tebakan = {}
    list_kandang = []

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKRED = '\033[91m'

    def menu(self):
        print("-"*40+"\n"+" "*13+self.OKBLUE+"Tebak Kandang"+self.ENDC+"\n"+"-"*40+"\n"+
        "1. Jumlah Kandang"+"\n"+"99. Exit"+"\n"+"-"*40+"\n")
        self.inputs = input("pilih menu:")
        if self.inputs == '1':
            return self.sesi_tampilkan_kandang()
        elif self.inputs == '99':
            print('Bye')
    
    def sesi_tampilkan_kandang(self):
        self.jumlah_kandang = input("Masukkan jumlah kandang:")
        for self.i in range(1,int(self.jumlah_kandang)+1):
            self.tebakan[self.i] = random.choice(self.list_hewan)
            self.list_kandang.append(super().nomor(self.i))
        
        print(''.join(self.list_kandang))
        return self.sesi_pilih_kandang()
    
    def sesi_pilih_kandang(self):
        if self.tebakan == {}:
            print(self.OKGREEN+"Selamat! anda menebak semua kandang"+self.ENDC)
        else:
            self.pilih_nomor_kandang = input("Pilih kandang yang ingin dibuka:")
            print("---PILIHAN---"+"\n"+self.OKBLUE+"K"+self.ENDC+": Kambing"+"\n"+self.OKRED+"Z"+self.ENDC+": Zebra"+"\n"+self.OKYELLOW+"B"+self.ENDC+": Bebek"+"\n")
            return self.sesi_tebak_kandang(self.pilih_nomor_kandang)
        
    def sesi_tebak_kandang(self,pilih_nomor_kandang):   
        self.tebak_isi_kandang = input("Masukan tebakan:")
        print(self.UNDERLINE+"PERCOBAAN"+self.ENDC+" "+self.UNDERLINE+"BUKA:"+self.ENDC+"\n")
        for self.i in range(1,int(self.jumlah_kandang)+1):
            if self.i == int(pilih_nomor_kandang):
                if self.tebak_isi_kandang == 'K':
                    self.list_kandang[self.i-1] = super().kambing()
                elif self.tebak_isi_kandang == 'Z':
                    self.list_kandang[self.i-1] = super().zebra()
                elif self.tebak_isi_kandang == 'B':
                    self.list_kandang[self.i-1] = super().bebek()      
        
        print(''.join(self.list_kandang))
        return self.sesi_penentuan_isi_tebakan()
    
    def sesi_penentuan_isi_tebakan(self):
        if self.tebakan[int(self.pilih_nomor_kandang)] == self.tebak_isi_kandang:
            print(self.OKGREEN+"Tebakan Benar!"+self.ENDC+"\n")
            print(''.join(self.list_kandang))
            del self.tebakan[int(self.pilih_nomor_kandang)]
            return self.sesi_pilih_kandang()
        else:
            print(self.OKYELLOW+"Tebakan salah"+self.ENDC+"\n")
            self.list_kandang[int(self.pilih_nomor_kandang)-1] = super().nomor(self.pilih_nomor_kandang)
            print(''.join(self.list_kandang))
            return self.sesi_pilih_kandang()

main = Board()
main.menu()
        
