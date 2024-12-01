from . import Operasi


def read_console():
	data_file = Operasi.read()
	index = "No"
	judul = "Judul"
	penulis = "Penulis"
	tahun = "Tahun"

	# header
	print( '=' * 100 )
	print( f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}" )
	print( 100 * '=' )
	print( "Data" )

	# Data
	for index, data in enumerate( data_file ):
		data_break = data.split( "," )
		print( data_break )

	# footer
	print( 100 * '=', '\n' )
