def howManyGifts(maxBudget, gifts) :
    swapped = True
    while swapped:
        swapped = False
        maxIter = len(gifts)-1
        for i in range(maxIter):
            val1 = gifts[i]
            val2 = gifts[i+1]
            if val1>val2:
                gifts[i] = val2
                gifts[i+1] = val1
                swapped = True
    count=0
    
    while maxBudget >0:
        if maxBudget>=gifts[count]:
            count+=1
            maxBudget = maxBudget-gifts[count-1]
        else:
            maxBudget = maxBudget-gifts[count]
        
    return count 

print(howManyGifts(30000, [15000, 12000, 5000, 3000, 10000])) # 4
print(howManyGifts(10000, [2000, 2000, 3000, 1000, 2000, 10000])) # 5
print(howManyGifts(4000, [7500, 1500, 2000, 3000])) # 2
print(howManyGifts(50000, [25000, 25000, 10000, 15000])) # 3
print(howManyGifts(0, [10000, 3000])) # 0
