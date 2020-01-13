def angkaPalindrome(num):

    def cekPalindrome(num):
        digit = 1 # untuk menghitung jumlah digit angka tanpa fungsi string
        while num>=10**digit:
            digit+=1

        lst = [] # list untuk pecahan tiap digit num
        for i in range(digit-1,-1,-1):
            lst.append(int(num/(10**i)))
            num = num - int(num/(10**i))*10**i
        
        for i in range(int(len(lst)/2)): # untuk cek suatu angka palindrome atau bukan
            if lst[i] == lst[-i-1]: # cek pasangan digit angka harus sama untuk palindrome
                x = True
            else:
                x = False # jika ada min 1 pasangan tidak sama maka num bukan palindrom
                break
        return x
    
    num+=1
    if num<10:
        return num # jika bilangan setelah num berdigit 1 maka return bil. palindrome digit 1
    else:
        if cekPalindrome(num) == True: # jika bilangan setelah num palindrome, maka return nilai setelah bilangan num
            return num
        
        while  cekPalindrome(num) == False: # menampilkan bil. palindrome setelah num
            num+=1
            if cekPalindrome(num) == False:
                continue
            else:
                return num

print(angkaPalindrome(8))
print(angkaPalindrome(10))
print(angkaPalindrome(117))
print(angkaPalindrome(175))
print(angkaPalindrome(1000))




