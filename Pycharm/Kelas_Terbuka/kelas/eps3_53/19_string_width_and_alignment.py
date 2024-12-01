# width and multiline

data_nama = "Gompar"
data_umur = 30
data_sepatu = 42
data_tinggi = 170.18

data_string = f"nama = {data_nama}, umur = {data_umur}, sepatu = {data_sepatu}, tinggi = {data_tinggi}"
print( 5 * "=" + "Data String" + 5 * "=" )
print( data_string )

data_string = f"\nnama = {data_nama}, \numur = {data_umur}, \nsepatu = {data_sepatu}, \ntinggi = {data_tinggi}"
print( 5 * "=" + "Data String" + 5 * "=" )
print( data_string )

data_string = f'''
nama    = {data_nama:>10}
umur    = {data_umur:>10}
sepatu  = {data_sepatu:>10}
tinggi  = {data_tinggi:>10}
'''

print( 5 * "=" + "Data String" + 5 * "=" )
print( data_string )
