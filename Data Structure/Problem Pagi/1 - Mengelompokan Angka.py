def mengelompokkanAngka(arr):
    list_genap = []
    list_ganjil = []
    list_times3 = []
    list_hasil = []

    for i in arr:
        if i%2 == 0 and i%3 !=0 :
            list_genap.append(i)
        elif i%2 == 1 and i%3 != 0:
            list_ganjil.append(i)
        elif i%3 == 0:
            list_times3.append(i)
    
    arr = [list_genap, list_ganjil,list_times3]
    return arr

print(mengelompokkanAngka([2, 4, 6]))
# [ [2, 4], [], [6] ]
print(mengelompokkanAngka([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# [ [ 2, 4, 8 ], [ 1, 5, 7 ], [ 3, 6, 9 ] ]
print(mengelompokkanAngka([100, 151, 122, 99, 111]))
# [ [ 100, 122 ], [ 151 ], [ 99, 111 ] ]
print(mengelompokkanAngka([]))
# [ [], [], [] ]
