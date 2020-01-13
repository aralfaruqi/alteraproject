def changeMe(arr):
    for index,lst in enumerate(arr):
        if arr == []:
            print("")
        else:
            firstName = lst[0]
            lastName = lst[1]
            gender = lst[2]
            if len(lst) == 3:
                age = "Invalid Birth Year"
            elif len(lst) == 4 and 2019<lst[3]:
                age = "Invalid Birth Year"
            else:
                age = 2019 - lst[3]
            dict_bio = {'firstName':firstName,'lastName':lastName,'gender':gender,'age':age}
            print(f'{index+1} {firstName} {lastName}:')
            print(dict_bio)

changeMe([['Christ', 'Evans', 'Male', 1982], ['Robert', 'Downey', 'Male']])
changeMe([])
