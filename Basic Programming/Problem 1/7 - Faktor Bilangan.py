def faktor_bilangan(bil): 
    list_bil = []
    for i in range (1,bil+1): 
        if bil%i == 0: 
            list_bil.append(i) 
    print(*list_bil)

faktor_bilangan(6)
faktor_bilangan(12)
faktor_bilangan(14)
faktor_bilangan(16)
faktor_bilangan(20)