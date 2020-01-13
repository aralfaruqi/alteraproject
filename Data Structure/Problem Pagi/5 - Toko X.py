def countProfit(shoppers):
    listBarang = [ 
         ['Sepatu Stacattu', 1500000, 10], 
         ['Baju Zoro', 500000, 2], 
         ['Sweater Uniklooh', 175000, 1], 
         ]
    
    list_hasil = []

    for barang in listBarang:
        jumlah_beli = 0
        dict_product = {}
        list_shoppers = []
        for pembeli in shoppers:
            if pembeli['product'] == barang[0]:
                if barang[2]>=pembeli['amount']:
                    jumlah_beli+=pembeli['amount']
                    list_shoppers.append(pembeli['name'])
                    barang[2] = barang[2]-pembeli['amount']
        
        dict_product = {'product':barang[0],
        'shoppers':list_shoppers,
        'leftOver':barang[2],
        'totalProfit':jumlah_beli*barang[1]}
        list_hasil.append(dict_product)

    return list_hasil

print(countProfit([
 {'name': 'Windi', 'product': 'Sepatu Stacattu', 'amount': 2},
 {'name': 'Vanessa', 'product': 'Sepatu Stacattu', 'amount': 3},
 {'name': 'Rani', 'product': 'Sweater Uniklooh', 'amount': 2}
]))

print(countProfit([
 {'name': 'Windi', 'product': 'Sepatu Stacattu', 'amount': 8},
 {'name': 'Vanessa', 'product': 'Sepatu Stacattu', 'amount': 10},
 {'name': 'Rani', 'product': 'Sweater Uniklooh', 'amount': 1},
 {'name': 'Devi', 'product': 'Baju Zoro', 'amount': 1},
 {'name': 'Lisa', 'product': 'Baju Zoro', 'amount': 1}
]))

print(countProfit([{'name': 'Windi', 'product': 'Sepatu Naiki', 'amount': 5}]))

        





