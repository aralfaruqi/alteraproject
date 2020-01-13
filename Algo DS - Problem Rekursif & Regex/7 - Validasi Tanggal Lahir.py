import re

def tahun_kabisat(tahun):
    if tahun%400 == 0:
        return True
    elif tahun%4 == 0 and tahun%100 != 0:
        return True
    else:
        return False

def validasiTanggalLahir(arr):
    tahun_regex = re.compile(r'^(19|20)([0-9]{2})')
    for data in arr:
        if tahun_kabisat(int(tahun_regex.search(data['tgl_lahir']).group())):
            bulan_regex = re.compile(r'-((0[1-9]|1[0-2]))-')
            if str(bulan_regex.search(data['tgl_lahir']).group(1)) == '02' :
                tanggal_regex = re.compile(r'-(0[1-9]|[1-2][0-9])')
                if str(tanggal_regex.search(data['tgl_lahir']).group(1)):
                    



print(validasiTanggalLahir([
  {'nama':'Jane Doe', 'tgl_lahir': '1994-10-31'},
  {'nama':'Jack Doe', 'tgl_lahir': '1997-02-29'},
  {'nama':'Donny Doe', 'tgl_lahir': '1989-12-01'}
]))