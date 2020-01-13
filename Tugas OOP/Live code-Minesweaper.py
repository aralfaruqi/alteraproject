import sys
import os
import random

class Cell:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKRED = '\033[91m'

    def regular_cell(self):
        return " "
    
    def mine_cell(self):
        return self.OKRED+"!"+self.ENDC
    
    def bonus_cell(self):
        return self.OKYELLOW+"$"+self.ENDC

class Board(Cell):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKRED = '\033[91m'

    list_board_cell = [" "]
    __score = 0
    list_isi_cell = []
    macam_cell = []

    def header(self):
        print("-"*30+"\n"+" "*8+"Guess Games"+"\n"+"-"*30+"\n")
        print("1. Board Size"+"\n"+"2. Choose Cell"+"\n"+"98. Refresh Board"+"\n"+"99. Exit"+"\n"+"-"*30)
        return self.pilihan_menu()
        

    def pilihan_menu(self):
        self.input_pilihan = input("Masukan Pilihan Anda: ")

        if self.input_pilihan == '1':
            return self.buat_board()
        elif self.input_pilihan == '2':
            return self.pilih_cell()
        elif self.input_pilihan == '98':
            os.system('clear')
            self.list_board_cell = [" "]
            self.__score = 0
            return self.header()
        elif self.input_pilihan == '99' :
            print("Good Bye")

    def buat_board(self):
        self.jumlah_kolom = input("Masukan Jumlah Kolom: ")
        self.jumlah_baris = input("Masukan Jumlah Baris: ")

        for k in range(1,int(self.jumlah_kolom)+1):
            self.list_board_cell.append(self.OKGREEN+str(k)+self.ENDC )
        self.list_board_cell.append("\n")
        self.macam_cell.append(super().mine_cell())
        self.macam_cell.append(super().regular_cell())
        self.macam_cell.append(super().bonus_cell())

        for i in range(1,int(self.jumlah_baris)+1):
            self.list_board_cell.append(self.OKGREEN+str(i)+self.ENDC)
            for j in range(1,int(self.jumlah_kolom)+1):
                self.list_board_cell.append('X')
                self.list_isi_cell.append(random.choice(self.macam_cell))

            self.list_board_cell.append("\n")
        print("score: "+str(self.__score))
        print("".join(self.list_board_cell))
        return self.pilihan_menu()
    
    def pilih_cell(self):
        self.pilih_kolom = input("Masukkan kolom yang akan dibuka: ")
        self.pilih_baris = input("Masukkan baris yang akan dibuka: ")

        if self.list_isi_cell[(int(self.pilih_baris)-1)*int(self.pilih_kolom)+int(self.pilih_kolom)-1] == super().mine_cell():
            self.__score = self.__score - 10
            self.list_board_cell[int(self.pilih_baris)*(int(self.jumlah_kolom)+2)+int(self.pilih_kolom)] = super().mine_cell()
            print(self.OKYELLOW+"Mine - cell"+self.ENDC)
            print("score: "+str(self.__score))
            print("".join(self.list_board_cell))
        
        elif self.list_isi_cell[(int(self.pilih_baris)-1)*int(self.pilih_kolom)+int(self.pilih_kolom)-1] == super().regular_cell():
            self.list_board_cell[int(self.pilih_baris)*(int(self.jumlah_kolom)+2)+int(self.pilih_kolom)] = super().regular_cell()
            print(self.OKYELLOW+"Regular cell"+self.ENDC)
            print("score: "+str(self.__score))
            print("".join(self.list_board_cell))
            
        elif self.list_isi_cell[(int(self.pilih_baris)-1)*int(self.pilih_kolom)+int(self.pilih_kolom)-1] == super().bonus_cell():
            self.__score = self.__score+10
            self.list_board_cell[int(self.pilih_baris)*(int(self.jumlah_kolom)+2)+int(self.pilih_kolom)] = super().bonus_cell()
            print(self.OKYELLOW+"Bonus cell - Woow"+self.ENDC)
            print("score: "+str(self.__score))
            print("".join(self.list_board_cell))
        
        if self.list_board_cell.count("X") == 0:
            print(self.OKRED+"GAME OVER !!!"+self.ENDC)
    
        return self.pilihan_menu()

main = Board()
main.header()
        

        


        
        
        



    


                
                
                

    