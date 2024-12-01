# Operasi manipulasi list

data_list = ['sendok', 'piring', 'gelas', 'wajan']

# data_0 = data_list[0]
print('data pertama (index 0) adalah = ', data_list[0])
print('data pertama (index 1) adalah = ', data_list[1])
print('data pertama (index 0) adalah = ', data_list[-2])
print('data pertama (index -1) adalah = ', data_list[-1])

# mengambil jumlah data pada list
print('panjang data pada list =', len(data_list))

# manipulasi data list

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditabah = {data_list}")

data_list.insert(1, "kuali")
print(f"data setelah ditabah = {data_list}")

# menambah data di akhir list
data_list.append("kompor")
print(f"data setelah ditabah = {data_list}")

# menambahkan data baru
data_list_baru = ['bawang', 'tepung', 'kecap', 'kerupuk']
data_list.extend(data_list_baru)
print(f"data list baru  =\n {data_list}")

# merubah data
# ubah data index ke 2 di dalam list
data_list[2] = "Piwwwriinnkk"
print(f"ubah data idex ke 2 =\n {data_list}")

# remove data
data_list.remove("wajan")
data_list.remove("kecap")
data_list.remove("sendok")

print(f"remove data ={data_list}")

# remove data paling belakang
data_list.pop()
print(f"remove data paling belakang = {data_list}")
