# -----List -----

# list number
data_angka = [1, 2, 3, 4, 8]
print('data angka =', data_angka)

# list string
data_string = ['piring', 'gelas', 'sendok', 'wajan']
print('data string =', data_string)

# list boolean
data_boolean = [True, False, False, True, True]
print('data_boolean =', data_boolean)

# list campuran
data_campuran = [1, 'bala-bala', 2, 'cireng', 'sendok', False]
print(data_campuran)

# cara alternatif membuat List
data_list = list(range(0, 10))
print('data List menggunakan range =', data_list)

# membuat list dengab Loop, List comprehension
list_pake_for = [i ** 2 for i in range(0, 10)]
print('data list pake for = ', list_pake_for)

# list pake for pake if
list_pake_for_pake_if = [i for i in range(0, 10) if i != 5]
print('data list pake for pake if = ', list_pake_for_pake_if)

list_pake_for_pake_if = [i for i in range(0, 10) if i % 2 == 0]
print('data list pake for pake if genap = ', list_pake_for_pake_if)

list_pake_for_pake_if = [i for i in range(0, 10) if i % 2 != 0]
print('data list pake for pake if ganjil= ', list_pake_for_pake_if)
