# operator dalam bentuk method
# merubah case dari string

# uppercase
salam = "bro!"
print('normal  =', salam)
salam = salam.upper()
print('upper   =', salam)

# lowercase
alay = 'lOe kEchEEEE aBiiieezzz'
print('normal  = ', alay)
alay = alay.lower()
print('lower   = ', alay)

# pengecekan dengan menggunakan isX method
salam = "sist"
apakah_lower = salam.islower()
print(salam, " is lower = ", str(apakah_lower))
apakah_upper = salam.isupper()
print(salam, " is lower = ", str(apakah_upper))

# isalpha() cek semua huruf
# isalnum() cek huruf dan angka
# isdecimal() angka saja
# isspace() cek spasi, tab, newline \n
# istitle() semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okray 8"
cek_judul = judul.istitle()
print(judul, "Is Title = ", str(cek_judul))

# mengecek komponen startswith() endswith()
cek_start = "Hallo Selamat Pagi".startswith("Hallo")
print("Start = ", str(cek_start))

cek_end = "Hallo Selamat Pagi".endswith("Pagi")
print("End = ", str(cek_end))

print(10 * '=')
# penggabungan komponen join() dan split()
pisah = ['aku', 'sayang', 'kamu']
gabung = ','.join(pisah)
print(gabung)
gabung = ' '.join(pisah)
print(gabung)
gabung = ' ehm '.join(pisah)
print(gabung)

print(10 * '=')

gabung = "akuehmsayangehmkamu".split("ehm")
print(gabung)

# alokasi karakter rjust(), ljust(), center()
kanan = 'kanan'.rjust(30)
print("'", kanan, "'")
kiri = 'kiri'.ljust(30)
print("'", kiri, "'")
tengah = 'tengah'.center(30, '-')
print("'", tengah, "'")

# strip() mengilangkan semua karakter yang mau di hilangkan
tengah = tengah.strip("-")
print(tengah)
