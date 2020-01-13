def bil_prima(bil): 
    count = 0 
    for i in range(1,bil+1): 
        if bil%i == 0: 
            count+=1 
        else: 
            continue 
        
    if count == 2: 
        print("Bilangan Prima") 
    else : 
        print("Bukan Bilangan Prima")

bil_prima(3)
bil_prima(7)
bil_prima(10)