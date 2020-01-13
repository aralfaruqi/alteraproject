def groupAnimals(animals):
    huruf_awal = []
    for hewan in animals:
        huruf_awal.append(hewan[0])
    
    set_huruf_awal = set(huruf_awal)
    list_huruf_awal = list(set_huruf_awal)
    list_akhir = []

    swapped = True
    while swapped:
        swapped = False
        maxIter = len(list_huruf_awal)-1
        for i in range(maxIter):
            val1 = list_huruf_awal[i]
            val2 = list_huruf_awal[i+1]
            if val1>val2:
                list_huruf_awal[i] = val2
                list_huruf_awal[i+1] = val1
                swapped = True

    for huruf in list_huruf_awal:
        lst = []
        for hewan in animals:
            if huruf == hewan[0]:
                lst.append(hewan)

        list_akhir.append(lst)  
        
    return list_akhir

# Driver Code
print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil']))
# [ ['ayam', 'anoa'], ['cacing'], ['kuda', 'kancil'] ]
print(groupAnimals(['cacing', 'ayam', 'kuda', 'anoa', 'kancil', 'unta', 'cicak' ]))
# [ ['ayam', 'anoa'], ['cacing', 'cicak'], ['kuda'], ['unta'] ]


