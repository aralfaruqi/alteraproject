def digitPerkalianMinimum(angka):

    list_bil = [] # list untuk mengisi faktor bilangan dari angka
    for i in range (1,angka+1):  
        if angka%i == 0: 
            list_bil.append(i) # tiap faktor bilangan ditambahkan ke dalam list_bil
    
    list_jumlah_digit = [] # list untuk mengisi jumlah digit dari setiap faktor angka

    for i in list_bil:
        list_jumlah_digit.append(len(str(i))) # tiap jumlah digit faktor bilangan ditambahkan

    
    list_jumlahdigit_hasilkali = []  # list untuk mengisi jumlah dari pasangan hasil kali

    if len(list_jumlah_digit) == 1: # jika input angka adalah bil. kuadrat < 10
        return 2
    else:
        if len(list_jumlah_digit)%2 == 0: # jika input angka bil. bukan kuadrat >=10
            for i in range(int(len(list_jumlah_digit)/2)):
                list_jumlahdigit_hasilkali.append(list_jumlah_digit[i]+list_jumlah_digit[-i-1])
            
            minimum = list_jumlahdigit_hasilkali[0]
            for n in list_jumlahdigit_hasilkali: # Looping untuk mencari nilai min. dari jumlah
                if n < minimum:                  # pasangan hasil kali
                    minimum = n
            return minimum


        else:
            for i in range(int(len(list_jumlah_digit)/2)): # jika input angka bil. kuadrat > 10
                list_jumlahdigit_hasilkali.append(list_jumlah_digit[i]+list_jumlah_digit[-i-1])
            list_jumlahdigit_hasilkali.append(2*list_jumlah_digit[int(len(list_jumlah_digit)/2)])
            minimum = list_jumlahdigit_hasilkali[0]
            for n in list_jumlahdigit_hasilkali: # Looping untuk mencari nilai min. dari jumlah
                if n < minimum:                  # pasangan hasil kali
                    minimum = n
            return minimum

    
print(digitPerkalianMinimum(24))
print(digitPerkalianMinimum(90))
print(digitPerkalianMinimum(20))
print(digitPerkalianMinimum(179))
print(digitPerkalianMinimum(1))


        

        

    

    