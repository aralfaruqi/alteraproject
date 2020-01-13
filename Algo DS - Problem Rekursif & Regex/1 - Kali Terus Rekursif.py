def kaliTerusRekursif(angka):
    if len(str(angka)) == 1:
        return angka

    lst = list(str(angka))
    result = 1
    for i in lst:
        result = result*int(i)
    
    return kaliTerusRekursif(result)

print(kaliTerusRekursif(66)) # 8
print(kaliTerusRekursif(3)) # 3
print(kaliTerusRekursif(24)) # 8
print(kaliTerusRekursif(654)) # 0
print(kaliTerusRekursif(1231)) # 6

