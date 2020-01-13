def check_AB(kalimat): 
    list_a = [] 
    list_b = [] 
    list_ab = [] 
    
    for i in range(len(kalimat)): 
        if kalimat[i] == "a": 
            list_a.append(i) 
            
    for i in range(len(kalimat)): 
        if kalimat[i] == "b": 
            list_b.append(i) 
            
    for a in list_a: 
        for b in list_b: 
            list_ab.append(a-b) 
            
    if 4 in list_ab or -4 in list_ab: 
        x = True 
    else : 
        x =False 
    
    print(x)

check_AB("lane borrowed")
check_AB("i am sick")
check_AB("you are boring")
check_AB("barbarian")
check_AB("bacon and meat")