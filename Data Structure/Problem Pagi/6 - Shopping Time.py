def shoppingTime(memberId, money):
    list_barang = [ 
         ['Sepatu Stacattu', 1500000], 
         ['Baju Zoro', 500000], 
         ['Baju H&N',250000],
         ['Sweater Uniklooh', 175000], 
         ['Casing Handphone',50000]
         ]
    
    list_beli = []
    kamus = {}
    if memberId == '':
        return "Mohon maaf, toko X hanya berlaku untuk member saja"
    elif money<50000:
        return "Mohon maaf, uang tidak cukup"
    
    kamus['memberId'] = memberId
    kamus['money'] = money
    listPurchased = []

    for barang in list_barang:
        if money>=barang[1]:
            listPurchased.append(barang[0])
            money = money - barang[1]
            
    kamus['listPurchased'] = listPurchased
    kamus['changeMoney'] = money

    return kamus

print(shoppingTime('1820RzKrnWn08', 2475000))
print(shoppingTime('82Ku8Ma742', 170000))
print(shoppingTime('', 2475000))
print(shoppingTime('234JdhweRxa53', 15000))
print(shoppingTime('', ''))



   

