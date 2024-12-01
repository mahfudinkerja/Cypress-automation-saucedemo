import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")
print(f"Hari ini adalah hari = {hari_ini:%C}")

tanggal = dt.date(1994, 10, 1)
print(tanggal)
print(f"Hari ini adalah hari : {tanggal:%A}")

print(10 * "=" + "aplikasi nama hari" + 10 * "=")

print("Silahkan masukan tanggal, bulan, dan tahun kelahiran anda ^^")
tanggal = int(input("Tanggal \t : "))
bulan = int(input("Bulan \t\t : ")) 
tahun = int(input("Tahun \t\t : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
hari_ini = dt.date.today()

print(f"hari ini tanggal: {hari_ini}")
print(f"Tanggal lahir anda adalah: {tanggal_lahir}")

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")











