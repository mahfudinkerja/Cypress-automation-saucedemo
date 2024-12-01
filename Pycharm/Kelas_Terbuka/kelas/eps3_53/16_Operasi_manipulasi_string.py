nama_depan = "Monkey"
nama_tengah = "D"
nama_belakang = "Luffy"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_belakang
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# cek apakah ada komponen char atau string di dalam string
d = 'd'
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = 'D'
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = 'd'
status = d not in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

# Mengulang string
print(20 * "wk")
print("wk" * 20)

# indexing
print("index ke-0 :" + nama_lengkap[0])
print("index ke-1 :" + nama_lengkap[1])
print("index ke-(-1) :" + nama_lengkap[-1])
print("index ke-[0:5] :" + nama_lengkap[0:6])
print("index ke-[5:9] :" + nama_lengkap[5:9])
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah ", ascii_code)
data = 82
print("Char unruk ASCII code 117 adalah ", chr(data))

print(20 * "wk")

data = "otong surootong weleh totong ule ule tong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))
