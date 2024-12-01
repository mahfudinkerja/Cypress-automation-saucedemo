# nested list = didalam list ada list

data_0 = [1, 2]
data_1 = [3, 4, 5]

data_list_biasa = [1, 2, 3, 4, 5, 6]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1, data_list_biasa, 7, 8, 9, 0]
print(f"list 2D = {list_2D}")

# Contoh penggunaan
peserta_0 = ['ucup', 20, 'bekasi']
peserta_1 = ['otong', 22, 'jakarta']
peserta_2 = ['dadang', 28, 'bandung']

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t : {peserta[0]}")
    print(f"umur\t : {peserta[1]}")
    print(f"kota\t : {peserta[2]}\n")
