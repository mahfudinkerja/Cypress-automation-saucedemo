# Operasi komparasi

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih Dari >
print("=========Lebih Dari (>)")
hasil = a > 3
print(a, '>', 3, "=", hasil)

hasil = b > 3
print(b, '>', 3, "=", hasil)

hasil = b > 2
print(b, '>', 2, "=", hasil)

# Kurang Dari <
print("=========Kurang Dari (<)")
hasil = a < 3
print(a, '<', 3, "=", hasil)

hasil = b < 3
print(b, '<', 3, "=", hasil)

hasil = b < 2
print(b, '<', 2, "=", hasil)

# Lebih Dari sama dengan >=
print("=========Lebih Dari Sama dengan (>=)")
hasil = a >= 3
print(a, '>=', 3, "=", hasil)

hasil = b >= 3
print(b, '>=', 3, "=", hasil)

hasil = b >= 2
print(b, '>=', 2, "=", hasil)

# Kurang Dari sama dengan >=
print("=========Kurang Dari Sama dengan (<=)")
hasil = a <= 3
print(a, '<=', 3, "=", hasil)

hasil = b <= 3
print(b, '<=', 3, "=", hasil)

hasil = b <= 2
print(b, '<=', 2, "=", hasil)

# Sama dengan ==
print("=========Sama dengan (==)")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# Tidak Sama dengan !=
print("=========Tidak Sama dengan (!=)")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# "is" sebagai komparasi object identity
print("=========Object Komparasi (is)")

x = 5
y = 5

print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print(x, "is", y, hasil)

x = 5
y = 4

print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is y
print(x, "is", y, hasil)

print("=========Object Komparasi (is not)")

x = 5
y = 5

print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print(x, "is", y, hasil)

x = 5
y = 4

print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(y)))
hasil = x is not y
print(x, "is", y, hasil)
