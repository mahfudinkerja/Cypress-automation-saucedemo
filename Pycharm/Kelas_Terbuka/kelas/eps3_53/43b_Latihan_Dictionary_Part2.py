import datetime
import string
import random

mahasiswa_template = \
	{
		'nama': 'nama',
		'nim': '00000000',
		'sks_lulus': 0,
		'lahir': datetime.datetime( 1111, 11, 11 )
	}

data_mahasiswa = { }
while True:
	print( f"{'SELAMAT DATANG': ^20}" )
	print( f"{'DATA MAHASISWA': ^20}" )
	print( '-' * 20 )

	mahasiswa = dict.fromkeys( mahasiswa_template.keys() )
	# print( mahasiswa )

	mahasiswa[ 'nama' ] = input( 'Nama Mahasiswa = ' )
	mahasiswa[ 'nim' ] = input( 'Nim Mahasiswa = ' )
	mahasiswa[ 'sks_lulus' ] = int( input( 'SKS Mahasiswa = ' ) )
	tahun_lahir = int( input( "Tahun Lahir (YYYY) = " ) )
	bulan_lahir = int( input( "Bulan Lahir (MM) = " ) )
	tanggal_lahir = int( input( "Tanggal Lahir (DD) = " ) )
	mahasiswa[ 'lahir' ] = datetime.datetime( tahun_lahir, bulan_lahir, tanggal_lahir )

	# generate random key
	KEY = ''.join( (random.choice( string.ascii_uppercase ) for i in range( 6 )) )
	data_mahasiswa.update( { KEY: mahasiswa } )

	print( f"{'KEY':<6} {'NAMA':<17} {'NIM':<15} {'SKS Lulus':<10} {'Tahun Lahir':<10}" )
	print( 60 * '-' )

	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa

		NAMA = data_mahasiswa[ KEY ][ 'nama' ]
		NIM = data_mahasiswa[ KEY ][ 'nim' ]
		SKS = data_mahasiswa[ KEY ][ 'sks_lulus' ]
		LAHIR = data_mahasiswa[ KEY ][ 'lahir' ].strftime( '%x' )

		print( f"{KEY:<6} {NAMA:<17} {NIM:<15} {SKS:^10} {LAHIR:<10}" )

	print( '\n' )
	is_done = input( 'Masih lanjut (y/n ? = ' )
	if is_done == 'n':
		break

print( '\n program selesai' )

#
# book_lists = []
# while True:
#     print("Please Input Book\'s data ^^")
#     title = input('Input Book\'s Title : ')
#     writer = input('Input Book\'s Writer : ')
#
#     the_books = [title, writer]
#     book_lists.append(the_books)
#
#     print("\n\n Data buku ")
#     for index, book in enumerate(book_lists):
#         print(f"No.{index + 1}  | {book[0]}\t | {book[1]}")
#
#     isContinue = input("Continue ? (y / n) : ")
#     if isContinue == 'n':
#         break
#
# print("Program finish ><")
