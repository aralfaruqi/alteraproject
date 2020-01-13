import re

def validasiLogin(email, password):
    database = [
    {'email':'johndoe@gmail.com', 'password': '123456'},
    {'email':'johndoe@yahoo.co.id', 'password': '123456'},
    {'email':'john_doe@gmail.com', 'password': 'asdfasdfds'}
    ] 

    hasil = {}

    password_regex = re.compile(r'[0-9a-zA-Z]{6,10}')
    kata_kunci = password_regex.search(password)
    email_regex = re.compile(r'[\w\.\-]+@[\w\.\-]+\.[\w\.]')
    surel = email_regex.search(email)

    if not surel:
        return {'pesan':['email tidak valid'],'status':False}
    
    if not kata_kunci:
        return {'pesan':['password tidak valid'],'status':False}

    for data in database:
        if data['email'] == email and data['password'] == password:
            hasil['pesan'] = []
            hasil['status'] = True
            break
        else:
            hasil['pesan'] = ['password tidak valid']
            hasil['status'] = False
    
    return hasil

print(validasiLogin('johndoe@gmail.com','123456'))
# {'pesan': [], 'status': True}
print(validasiLogin('jane@gmail.com','1245'))
# {'pesan': ['password tidak valid'], 'status': False
print(validasiLogin('johndoe_gmail.com','123456'))
# {'pesan': ['email tidak valid'], 'status': False}
print(validasiLogin('johndoe@yahoo.co.id','12abcd'))
# {'pesan': [password tidak valid], 'status': False}
print(validasiLogin('john_doe@gmail.com','asdfasdfds'))
# {'pesan': [], 'status': True}


