def tentukanDeretGeometri(arr):
    for i in range(1,len(arr)-1):
        if arr[i]**2 != arr[i-1]*arr[i+1]: # deret geometri jika tiap suku ke i-1 dan i+1
            x = False                      # sama dengan suku ke i pangkat 2
            break 
        else:
            x = True
    
    return x

print(tentukanDeretGeometri([1,3,9,27,81]))
print(tentukanDeretGeometri([2,4,8,16,32]))
print(tentukanDeretGeometri([2,4,6,8]))
print(tentukanDeretGeometri([2,6,18,54]))
print(tentukanDeretGeometri([1,2,3,4,7,9]))
