# Lambda function
def garis():
	print( 30 * '-' )


def f_kuadrat( angka ):
	return angka ** 2


print( f"Hasil fungsi kuadrat =  {f_kuadrat( 3 )}" )
garis()

# output = lambda argument: expression
kuadrat = lambda angka: angka ** 2
print( f"Hasil lambda kuadrat = {kuadrat( 5 )}" )

pangkat = lambda num, pow: num ** pow
print( f"Hasil lambda pangkat = {pangkat( 5, 1 )}" )

garis()
# sorting untuk list biasa
data_list = [ 'ucup', 'dudung', 'otong' ]
data_list.sort()
print( f'sorted list = {data_list}' )

data_list.sort( key = len )
print( f'sorted list by len = {data_list}' )

garis()
data_list = [ 'ucup', 'dudung', 'otong' ]
data_list.sort( key = lambda nama: len( nama ) )
print( f'sorted list by lambda = {data_list}' )

# filter
data_angka = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]


def kurang_dari_lima( angka ):
	return angka < 5


data_angka_baru = list( filter( kurang_dari_lima, data_angka ) )
print( f"bukan lambda =  {data_angka_baru}" )

data_angka_lambda = list( filter( lambda x: x < 7, data_angka ) )
print( f"data lambda =  {data_angka_lambda}" )

# kasus genap
data_genap = list( filter( lambda x: (x % 2 == 0), data_angka ) )
print( data_genap )

# kasus ganjil
data_ganjil = (list( filter( lambda x: (x % 2 != 0), data_angka ) ))
print( data_ganjil )

data_3 = (list( filter( lambda x: (x % 3 == 0), data_angka ) ))
print( data_3 )


# anonymous function
# currying <- Hansell curry

def pangkat( angka, n ):
	hasil = angka ** n
	return hasil


data_hasil = pangkat( 4, 2 )
print( f"fungsi biasa = {data_hasil}" )


def pangkat_new( n ):
	return lambda angka: angka ** n


pangkat2 = pangkat_new( 2 )
print( f"fungsi lambda pangkat 2 = {pangkat2( 5 )}" )

pangkat3 = pangkat_new( 3 )
print( f"fungsi lambda pangkat 3 = {pangkat3( 5 )}" )

print( f"fungsi lambda pangkat bebas = {pangkat_new( 5 )( 3 )}" )
