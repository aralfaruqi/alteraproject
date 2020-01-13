def pasanganTerbesar(num):
    lst = [] # list untuk pasangan tiap 2 angka dalam num
    for i in range(len(str(num))-1):
        lst.append(int(str(num)[i])*10+int(str(num)[i+1])) # tiap pasangan 2 angka ditambahkan
                                                           # ke dalam lst
    maks = 0
    for element in lst: # mencari nilai maksimum dari anggota lst
        if element > maks:
            maks = element
    
    return maks


        

print(pasanganTerbesar(641573))
print(pasanganTerbesar(12783456))
print(pasanganTerbesar(910233))
print(pasanganTerbesar(71856421))
print(pasanganTerbesar(79918293))


