def mostFrequentItem(arr) :
    set_item = set(arr)
    list_item = list(set_item)
    kamus = {}
    list_count = []
    hasil = []

    swapped = True
    while swapped:
        swapped = False
        maxIter = len(list_item)-1
        for i in range(maxIter):
            val1 = arr.count(list_item[i])
            val2 = arr.count(list_item[i+1])
            if val1>val2:
                temp = list_item[i+1]
                list_item[i+1] = list_item[i]
                list_item[i] = temp
                swapped = True
    
    for item in list_item:
        hasil.append(item+"("+str(arr.count(item))+")")
    
    hasil_akhir = ", ".join(hasil)
    return hasil_akhir
    
print(mostFrequentItem(['asus', 'asus', 'samsung', 'iphone', 'iphone', 'asus', 'asus']))
# 'samsung(1), iphone(2), asus(4)'
print(mostFrequentItem(['9', 'b', 'b', 'c', '9', '9', 'b', '9', '2', '2']))
# 'c(1), 2(2), b(3), 9(4)'
print(mostFrequentItem(['book', 'laptop', 'iPod']))
# 'book(1), laptop(1), iPod(1)'