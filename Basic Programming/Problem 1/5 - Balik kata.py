def fungsi_kata(kalimat):
    list_kalimat = kalimat.split() 
    list_kalimat_baru = [] 
    
    for kata_lama in list_kalimat: 
        kata_baru = [] 
        for i in range(len(kata_lama)-1,-1,-1): 
            kata_baru.append(kata_lama[i]) 
        gabung_kata = "".join(kata_baru) 
        list_kalimat_baru.append(gabung_kata) 
        
    balik_kata_baru = [] 
    for i in range(len(list_kalimat_baru)-1,-1,-1): 
        balik_kata_baru.append(list_kalimat_baru[i]) 
        
    print(*balik_kata_baru)

fungsi_kata("John Doe")
fungsi_kata("Hello World and Coders")