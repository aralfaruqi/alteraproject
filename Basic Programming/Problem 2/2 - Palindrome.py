def palindrome(kata):
    count = 0 # count untuk menghitung jumlah pasangan huruf yang sama
    for i in range(int(len(kata)/2)):  
        if kata[i] == kata[-i-1]: # jika huruf pasangan sama, count bertambah
            count+=1
        else:
            continue
    if count == int(len(kata)/2): # jumlah count harus sama dengan floor((panjang kata)/2)
        return True
    else:
        return False

print(palindrome('katak'))
print(palindrome('blanket'))
print(palindrome('civic'))
print(palindrome('kasur rusak'))
print(palindrome('mister'))

        
            
