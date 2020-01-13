def konversi(waktu): 
    if waktu/60 >= 1: 
        jam = int(waktu/60) 
    else: 
        jam = 0 
        
    menit = waktu%60 
    if menit<10: 
        print(str(jam)+":0"+str(menit)) 
    else: 
        print(str(jam)+":"+str(menit))

konversi(63)
konversi(124)
konversi(53)
konversi(88)
konversi(120)
