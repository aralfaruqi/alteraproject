def convertToCoin(value):
    lst = [] # list untuk menambahan tiap pecahan nilai uang dari value
    while value>=1:
        pecahan_uang = [10000,5000,2000,1000,500,200,100,50,20,10,1]
        for i in pecahan_uang:
            if int(value/i)>0:
                for n in range(int(value/i)):
                    lst.append(i) 
                value = value - i*int(value/i)

    return lst

print(convertToCoin(543))
print(convertToCoin(7752))
print(convertToCoin(37454))
        

