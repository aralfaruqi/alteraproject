def cariModus(arr) :
    lst = []
    for value in arr:
        lst.append(arr.count(value))
    max = lst[0]
    for i in range(1,len(arr)):
        if lst[i]>max:
            max = lst[i]
    
    if lst.count(max) == len(lst):
        return -1
    else:
        return arr[lst.index(max)]
        
print(cariModus((10, 4, 5, 2, 4))) # 4
print(cariModus((5, 10, 10, 6, 5))) # 5
print(cariModus((10, 3, 1, 2, 5))) # -1
print(cariModus((1, 2, 3, 3, 4, 5))) # 3
print(cariModus((7, 7, 7, 7, 7))) # -1
