def initialGroupingDescending(studentsArr) :
    huruf_awal = []
    for student in studentsArr:
        huruf_awal.append(student[0])
    
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
            if val1<val2:
                list_huruf_awal[i] = val2
                list_huruf_awal[i+1] = val1
                swapped = True

    for huruf in list_huruf_awal:
        lst = []
        lst.append(huruf)
        for student in studentsArr:
            if huruf == student[0]:
                lst.append(student)

        list_akhir.append(lst)  
        
    return list_akhir

print(initialGroupingDescending(['Budi', 'Badu', 'Joni', 'Jono']))
print(initialGroupingDescending(['Mickey', 'Yusuf', 'Donald', 'Ali', 'Gong']))
print(initialGroupingDescending(['Rock', 'Stone', 'Brick', 'Rocker', 'Sticker']))