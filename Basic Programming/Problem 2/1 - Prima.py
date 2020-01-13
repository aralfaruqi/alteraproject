def angkaPrima(angka): 
    count = 0 # count untuk menghitung jumlah faktor pembagi
    for i in range(1,angka+1): 
        if angka%i == 0: #jika habis membagi, jumlah faktor pembagi bertambah
            count+=1 
        else: 
            continue 
        
    if count == 2: 
        return True
    else : 
        return False

print(angkaPrima(1))
print(angkaPrima(3))
print(angkaPrima(7))
print(angkaPrima(6))
print(angkaPrima(23))

