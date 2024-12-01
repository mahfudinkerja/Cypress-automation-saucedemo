data_angka = [1, 4, 5, 7, 8, 9, 0, 6, 5, 4, 3, 5, 7, 8, 9, 3, 9, 0, 6, 5, 4, 3, 3]
print(f"data angka = {data_angka}")

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(5)

print(f"data 4 = {jumlah_data_4}, data 3 = {jumlah_data_3}")

# ambil posisi data (index)

data_dapur = ['sendok', 'ayam goreng', 'bakwan', 'wajan', 'ulekan', 'piring', 'gelas']

print(f"data index wajan = {data_dapur.index('wajan')}")
print(f"data index piring = {data_dapur.index('piring')}")

# mengurutkan list dari kecil ke besar
data_angka.sort()
data_dapur.sort()
print(f"data angka dan dapur sort =\n{data_angka} \n{data_dapur}")

# mengurutkan list dari besar ke kecil
data_angka.reverse()
data_dapur.reverse()
print(f"data angka dan dapur reverse = \n{data_angka} \n{data_dapur}")
