def targetTerdekat(arr): # asumsi input array hanya 'x',' ', dan 'o'
    index_x = []
    index_o = []

    for i in range(len(arr)): # looping untuk isi list index tiap x dan o ada dimana
        if arr[i] == 'x':
            index_x.append(i)
        elif arr[i] == 'o':
            index_o.append(i)

    if index_x == [] or index_o == []: # jika x atau o tidak ditemukan maka return 0
        return 0

    index_xo = []
    for i in index_x: # Looping untuk mengisi list jarak spasi antar karakter x dan o
        for n in index_o:
            y = i-n
            if y<0:
                y = (i-n)*(-1)
            index_xo.append(y)
    
    minimum = index_xo[0]

    for i in range(len(index_xo)): # # mencari nilai minimum dari list jarak spasi x dan o
        if index_xo[i] < minimum:
            minimum = index_xo[i]
    
    return minimum

print(targetTerdekat([' ',' ','o',' ',' ','x',' ','x']))
print(targetTerdekat(['o',' ',' ',' ','x','x','x']))
print(targetTerdekat(['x',' ',' ',' ','x','x','o',' ']))
print(targetTerdekat([' ',' ','o',' ']))
print(targetTerdekat([' ','o',' ','x','x',' ',' ','x']))
