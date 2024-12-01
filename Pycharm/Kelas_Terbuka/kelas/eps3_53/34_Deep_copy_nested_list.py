data_0 = [1, 2, 'mie ayam', '7']
data_1 = [3, 'bubur ayam']
data_2 = ['gelas', '8', 'sate']

data_2D = [data_0, data_1, data_2, 9]
print(f"data_2D      = {data_2D}")

data_2D_copy = data_2D.copy()
print(f"data_2D copy = {data_2D_copy}")

# mengambil data dari nested list
data_take_0 = data_2D[0][0]
data_take_1 = data_2D[1][1]
data_take_2 = data_2D[0][3]
data_take_3 = data_2D[2][2]

print(f"Ambil data dari data 2D =  {data_take_0}, {data_take_1}, {data_take_2}, {data_take_3}")

# address data (bungkus)
print(f"address data 2D      = {hex(id(data_2D))}")
print(f"address data 2D copy = {hex(id(data_2D_copy))}")

# address list (isi)
print(f"address list 2D      = {hex(id(data_2D[0][1]))}")
print(f"address list 2D copy = {hex(id(data_2D_copy[0][1]))}")

data_2D[0][1] = 'nasi rames'
data_2D[1][1] = 'bubar yayam'
print(f"data asli = {data_2D}")
print(f"data copy = {data_2D_copy}")

# Deep Copy [SOLUSI dicpy ampe dalem]
from copy import deepcopy

data_2D = [data_0, data_1, data_2, 9]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address data 2D          = {hex(id(data_2D))}")
print(f"address data 2D deepcopy = {hex(id(data_2D_deepcopy))}")

print(f"address list 2D          = {hex(id(data_2D[0]))}")
print(f"address list 2D deepcopy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[0][1] = 'nasi bebek'

print(f"data asli     : {data_2D}")
print(f"data copy     : {data_2D_copy}")
print(f"data deepcopy : {data_2D_deepcopy}")
