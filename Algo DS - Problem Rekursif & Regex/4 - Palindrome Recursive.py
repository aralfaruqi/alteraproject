def palindromeRecursive(sentence) :
    if len(sentence) ==0 or len(sentence) == 1:
        return 'true'
    elif sentence[0] == sentence[-1]:
        sentence = sentence[1:-1]
        return palindromeRecursive(sentence)
    else:
        return 'false'

# Driver Code
print(palindromeRecursive('katak')) # true
print(palindromeRecursive('blanket')) # false
print(palindromeRecursive('civic')) # true
print(palindromeRecursive('kasur rusak')) # true
print(palindromeRecursive('mister')) # false