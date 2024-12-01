# 1. mode write

# akan dibuatkan data file baru
# dan akan menimpa atau overwrite data yang terakhir
with open( 'data_1.txt', 'w', encoding = 'utf-8' ) as file:
	file.write( 'ucup surucup' )

with open( 'data_1.txt', 'w', encoding = 'utf-8' ) as file:
	file.write( 'Jhon si jhonny' )

with open( 'data_1.txt', 'w', encoding = 'utf-8' ) as file:
	file.write( 'gompar si gomgom' )

# mode append

with open( 'data_2.txt', 'w', encoding = 'utf-8' ) as file:
	file.write( 'gompar si gomgom \n' )

with open( 'data_2.txt', 'a', encoding = 'utf-8' ) as file:
	file.write( 'bella si belbel' )

with open( 'data_2.txt', 'a', encoding = 'utf-8' ) as file:
	file.write( 'apiii si ocill' )

# 3. menggunakan r+

with open( 'data_3.txt', 'w', encoding = 'utf-8' ) as file:
	file.write( 'data ke 3\n' )

with open( 'data_3.txt', 'r+', encoding = 'utf-8' ) as file:
	file.write( 'Baris ke-1\n' )
	file.write( 'Baris ke-2\n' )
	file.write( 'Baris ke-3' )

with open( 'data_3.txt', 'r+', encoding = 'utf-8' ) as file:
	data = file.read()
	print( data )

with open( 'data_3.txt', 'r+', encoding = 'utf-8' ) as file:
	data = file.write( 'Otong' )
	print( data )
