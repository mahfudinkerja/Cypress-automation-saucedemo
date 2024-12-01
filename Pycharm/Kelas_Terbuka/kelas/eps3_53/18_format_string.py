# Format string

# contoh generic
# String
nama = "ucup"
format_str = f"hello {nama} !"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan menampilkan koma (,)
angka = 1500000000
format_str = f"bilangan bulat = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"angka = {angka:.3f}"  # f adalah float nya
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"angka = {angka:029.3f}"  # f adalah float nya
print(format_str)

# menampilkan plus minus
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp.{harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print("\n")
print(format_binary)
print(format_octal)
print(format_hex)
