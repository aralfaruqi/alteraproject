def totalDigitRekursif(angka):
    if int(angka/10) == 0:
        return angka
    else:
        return angka%10 + totalDigitRekursif(int(angka/10))

print(totalDigitRekursif(512)) # 8
print(totalDigitRekursif(1542)) # 12
print(totalDigitRekursif(5)) # 5
print(totalDigitRekursif(21)) # 3
print(totalDigitRekursif(11111)) # 5

