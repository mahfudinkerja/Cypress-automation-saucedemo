import datetime

mahasiswa1 = {
	'nama': 'mapud',
	'nim': '1203021101',
	'sks_lulus': 100,
	'beasiswa': True,
	'lahir': datetime.datetime( 2005, 1, 29 )
}

mahasiswa2 = {
	'nama': 'gompar',
	'nim': '1203021102',
	'sks_lulus': 120,
	'beasiswa': True,
	'lahir': datetime.datetime( 2004, 12, 1 )
}

mahasiswa3 = {
	'nama': 'bella',
	'nim': '1203021103',
	'sks_lulus': 140,
	'beasiswa': False,
	'lahir': datetime.datetime( 2007, 8, 3 )
}

data_mahasiswa = {
	'MAH001': mahasiswa1,
	'MAH002': mahasiswa2,
	'MAH003': mahasiswa3
}

print( f"{'KEY':<6} {'Nama':<10} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}" )
print( 50 * '=' )

for mahasiswa in data_mahasiswa:
	KEY = mahasiswa

	NAMA = data_mahasiswa[ KEY ][ 'nama' ]
	NIM = data_mahasiswa[ KEY ][ 'nim' ]
	SKS = data_mahasiswa[ KEY ][ 'sks_lulus' ]
	BEASISWA = data_mahasiswa[ KEY ][ 'beasiswa' ]
	LAHIR = data_mahasiswa[ KEY ][ 'lahir' ].strftime( '%x' )

	print( f"{NIM:<6} {NAMA:<10} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}" )
