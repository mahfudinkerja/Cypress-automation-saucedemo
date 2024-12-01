# contoh untuk menangkap exception

# from math import nan

# input_user = int( input( 'Masukan Angka : ' ) )
# hasil = 0
#
# try:
# 	hasil = 10 / input_user
# except:
# 	print( 'Input tidak boleh 0' )
# print( f"hasil = {hasil}" )


while True:
	angka = int( input( 'Masukan angka pembagi : ' ) )
	try:
		hasil = 20 / angka
		print( f"hasil = {hasil}" )
		is_done = input( 'Mau lanjut (y/n) ? : ' )
		if is_done == 'n':
			break
	except:
		print( 'Pembagi nol, silahkan masukan input lagi' )

print( 'Akhir dari program' )

try:
	with open( 'data.txt', 'r' ) as file:
		print( file.read() )
except:
	print( 'file data.txt tidak ditemukan, membuat file baru' )
	with open( 'data.txt', 'w', encoding = 'utf-8' ) as file:
		file.write( 'file baru' )

print( 'akhir dari program 2' )
