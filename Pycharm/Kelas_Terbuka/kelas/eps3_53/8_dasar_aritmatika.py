# Operasi Aritmatika
a = 10
b = 3

# Tambah

hasil = a + b
print(a, '+', b, '=', hasil)

# Kurang
hasil = a - b
print(a, '-', b, '=', hasil)

# Kali
hasil = a * b
print(a, 'x', b, '=', hasil)

# Bagi
hasil = a / b
print(a, '/', b, '=', hasil)

# Eksponen pangkat
hasil = a ** b
print(a, '**', b, '=', hasil)

# Modulus
hasil = a % b
print(a, '%', b, '=', hasil)

# Floor division
hasil = a // b
print(a, '//', b, '=', hasil)

# Prioritas Operasi
'''
    1. ()
    2. Exponen **
    3. Perklian dan teman-teman * / % //
    4. Pertambahan dan pengurangan
'''

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x)

hasil2 = x + y * z
print(x, "+", y, "*", z, "=", hasil2)
