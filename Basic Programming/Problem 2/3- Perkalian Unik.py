def perkalianUnik(arr):
    hasilkali = 1
    lst = [] # list untuk hasil perkalian unik
    for n in range(len(arr)): # looping untuk mendapatkan hasil kali semua anggota list
        hasilkali = hasilkali*arr[n]
    for i in range(len(arr)):
        lst.append(int(hasilkali/arr[i])) # hasilkali dibagi tiap anggota arr dan ditambahkan ke lst
    return lst                            

print(perkalianUnik([2,4,6]))
print(perkalianUnik([1,2,3,4,5]))
print(perkalianUnik([1,4,3,2,5]))
print(perkalianUnik([1,3,3,1]))
print(perkalianUnik([2,1,8,10,2]))
