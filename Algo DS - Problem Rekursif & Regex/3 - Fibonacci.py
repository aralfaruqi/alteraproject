def fibonacci(angka):
    if angka == 0 or angka == 1:
        return angka
    elif angka>1:
        return fibonacci(angka-1)+fibonacci(angka-2)

print(fibonacci(0)) # 0
print(fibonacci(2)) # 1
print(fibonacci(9)) # 34
print(fibonacci(10)) # 55
print(fibonacci(12)) # 144

