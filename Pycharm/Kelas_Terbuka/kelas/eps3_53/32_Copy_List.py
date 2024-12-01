# Teknik menduplikat list

a = ['mie ayam', 'bakso', 'sate', 'gado-gado', 'nasi padang']
print(f"data list a = {a}")

b = a
print(f"data list b = {b}")

# rubah data list dari a
a[1] = 'es campur'
b.sort()
print(f"data list a = {a}")
print(f"data list b = {b}")

# cek address hex id
print(f"address data a = {hex(id(a))}")
print(f"address data b = {hex(id(b))}")

# copy data SOLUSI!
print(10 * '=')
c = a.copy()
print(f"address data a = {hex(id(a))}")  # sama
print(f"address data b = {hex(id(b))}")  # sama
print(f"address data c = {hex(id(c))}")  # berbeda

c[0] = 'es teler'
print(f"data list a :\n {a} \n {b} \n {c}")
