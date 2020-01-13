def bil_prima(bil): # fungsi untuk mengecek bilangan prima atau bukan
        count = 0 
        for i in range(1,bil+1): 
            if bil%i == 0: 
                count+=1 
            else: 
                continue 
        
        if count == 2: 
            return True 
        else : 
            return False

def primaSegiEmpat(P,L,X):
    
    X+=1
    total = 0

    for i in range(L): # print baris bilangan prima sebanyak L baris
        lst = [] # list untuk menambahkan bil. prima untuk tiap baris segi empat
        while len(lst) < P: # print kolom bilangan prima sebanyak P kolom
            if bil_prima(X) == True: # jika bilangan prima maka ditambahkan kedalam lst
                lst.append(X)
                total+=X # total dari seluruh segi empat bil. prima
            X+=1
    
        print(*lst)
    
    return "Total: " + str(total) 

print(primaSegiEmpat(2,3,13))
print(primaSegiEmpat(5,2,1))
        
