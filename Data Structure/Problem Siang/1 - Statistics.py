def statistik(kata, arr1, arr2):
    if kata == 'min':
        x1 = arr1[0]
        x2 = arr2[0]

        for i in range(1,len(arr1)):
            if arr1[i]<x1:
                x2 = arr[i]

        for i in range(1,len(arr2)):
            if arr2[i]<x2:
                x2 = arr2[i]
        
    elif kata == 'max':
        x1 = arr1[0]
        x2 = arr2[0]

        for i in range(1,len(arr1)):
            if arr1[i]>x1:
                x1 = arr1[i]

        for i in range(1,len(arr2)):
            if arr2[i]>x2:
                x2 = arr2[i]
    
    strx1 = str(x1)
    strx2 = str(x2)

    array = [strx1,strx2]
    arrays = " ".join(array)
    return arrays

print(statistik('min', [1, 1, 1] , [8, 15, 17, 9])) # 1 8
print(statistik('max', [4, 8, 9, 12] , [33, 88, 99 ,11])) # 12 99
print(statistik('min', [1, 2, 5, 2, 2] , [67, 45, 55])) # 1 45
print(statistik('max', [6, 2, 4, 10, 8, 2] , [6, 5, 13, 23])) # 10 23
print(statistik('min', [5, 11, 18, 6], [3, 1, 8, 13])) # 5 1
