# Args pada fungsi

# masukan data / argument
def garis():
	print( 50 * '-' )


def fungsi_1( nama, tinggi, berat ):
	print( f"si {nama} punya tinggi {tinggi}, dan berat {berat}" )


fungsi_1( 'Mapud', 173, 90 )
garis()


def fungsi_2( data_list ):
	data = data_list.copy()
	nama = data[ 0 ]
	tinggi = data[ 1 ]
	berat = data[ 2 ]
	print( f"si {nama} punya tinggi {tinggi}, dan berat {berat}" )


fungsi_2( [ 'Ucup', 153, 60 ] )

garis()


# menggunakan args

def fungsi_3( *args ):
	nama = args[ 0 ]
	tinggi = args[ 1 ]
	berat = args[ 2 ]
	print( f"si {nama} punya tinggi {tinggi}, dan berat {berat}" )


fungsi_3( 'Yanto', 163, 70 )


# studi kasus
def tambah( *data ):
	output = 0
	for angka in data:
		output += angka

	return output


print( f"hasil = {tambah( 1, 2, 3, 4, 5, 6, 7, 8, 9 )}" )
print( f"hasil = {tambah( 10, 2, 3 )}" )
