Ns = 5
N1 = int(Ns)

#Pattern satu
for i in range(1,N1+1):
    lst = []
    for n in range(i):
        lst.append("*")
    print(*lst)

#Pattern dua
for i in range(1,N1+1):
    lst = []
    for n in range(N1-i,0,-1):
        lst.append(" ")
    for m in range(i):
        lst.append(" *")
    print("".join(lst))

#Pattern tiga
for i in range(1,N1+1):
    lst = []
    for n in range(1,i+1):
        lst.append(n)
    print(*lst)

#Pattern empat
count = 0
for i in range(1,N1+1):
    lst = []
    for n in range(1,i+1):
        count+=1
        lst.append(count)
    print(*lst)

#Pattern lima
for i in range(1,N1+1):
    lst = []
    for n in range(N1-i,0,-1):
        lst.append(" ")
    for m in range(i):
        lst.append("*")
    print(*lst)

    

    
