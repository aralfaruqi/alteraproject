def kabisat(tahun):
    if tahun%4==0 and tahun%100!=0:
        return "Tahun kabisat"
    elif tahun%4==0 and tahun%100==0 and tahun%400==0: 
        return "Tahun kabisat"
    else: 
        return "Bukan tahun kabisat"

print(kabisat(1804))
print(kabisat(1803))
print(kabisat(2400))
print(kabisat(2490))
    