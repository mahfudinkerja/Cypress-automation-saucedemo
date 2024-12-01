# copy dictionary

makanan = {
	'nasgor': 'Nasi Goreng',
	'migor': 'Mie Goreng',
	'batagor': 'Bakso Tahu Goreng',
	'minas': 'Mie Nasi',
	'padang': 'Nasi Padang'
}

meal = makanan.copy()

print( f"makanan = {makanan}\n" )
print( f"meal = {meal}\n" )

makanan[ 'nasbek' ] = 'Nasi Bebek'
print( f"data makanan ditambahkan nasi bebek = {makanan} \n" )

# pop dictionary (berdasarkan key)
dataNasgor = makanan.pop( 'nasgor' )
print( f"Data Nasgor diambil dari List = {dataNasgor}" )
print( f"Makanan = {makanan}\n" )

# popitem dictionary
dataTerakhir = makanan.popitem()
print( f"Data Terakhir = {dataTerakhir}" )
print( f"Makanan = {makanan}\n" )
