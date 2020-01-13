import re

def cekDataTransaksi(logs):
        kamus = {}

        id_transaksi_regex = re.compile(r'Transaction #([0-9]{5})')
        id_transaksi = id_transaksi_regex.search(logs[0])
        id_order_regex = re.compile(r'trx_id = ([A-Z]+-[A-Z][a-z]+\|[A-Z]+-[0-9]{5})')
        id_order = id_order_regex.search(logs[2])
        nomor_seri_regex = re.compile(r'SN:([0-9]{20})')
        nomor_seri = nomor_seri_regex.search(logs[4])
        nomor_referensi_regex = re.compile(r'Ref Id. :([0-9]{9})')
        nomor_referensi = nomor_referensi_regex.search(logs[4])

        if nomor_seri:
            kamus['nomor_seri'] = f'{nomor_seri.group(1)}'
        else:
            kamus['nomor_seri'] = None
        
        kamus['id_transaksi'] = f'{id_transaksi.group(1)}'
        kamus['id_order'] = f'{id_order.group(1)}'
        

        if nomor_referensi:
            kamus['nomor_referensi'] = f'{nomor_referensi.group(1)}'
        else:
            kamus['nomor_referensi'] = None
        
        if kamus['nomor_referensi'] == None:
            kamus['success'] = False
        else:
            kamus['success'] = True

        return kamus
        

print(cekDataTransaksi([
    'Insert Transaction #14879',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx_id = YPSTRX-Indragiri|IDG-14879',
    'Transaction On Biller  type_modem arg: telkomsel_mobile queue_name arg: smtel-banyumas_mobile',
    'Success Manual SN:94309403940394039403 Ref Id. :394039403'
]))

print(cekDataTransaksi([
    'Insert Transaction #18254',
    'Update Status To Pending Payment With Deposit',
    'Transaction Paid trx_id = YPSTRX-Brebes|BYS-18254',
    'Transaction On Biller  type_modem arg: telkomsel_mobile queue_name arg: smtel-banyumas_mobile',
    'Trx. Cancel Process Begin | cancel trx with id18254',
    'Sukses Refunded trx id. 18254 with Wallet hash #eko827p7rk89m456'
]))



