""" Fungsi dengan argument"""


# # Template
# def nama_fungsi(argument / parameter):
# 	Badan Fungsi
def garis():
	print( 20 * '-' )


def hello_world( nama ):
	print( f"Selamat datang wahai {nama}" )


hello_world( 'apiii ocil' )
garis()


def tambah( angka_1, angka_2 ):
	hasil = angka_1 + angka_2
	print( f"{angka_1} + {angka_2} = {hasil}" )


tambah( 10, 1 )
tambah( 123123, 3456546 )
garis()


def say_hi( list_peserta ):
	list_peserta[ 1 ] = 'bakso'
	data_peserta = list_peserta.copy()
	for peserta in data_peserta:
		print( f"Hallo {peserta}" )


anggota_boyband = [ 'ucup', 'otong', 'dudung' ]
say_hi( anggota_boyband )
garis()
print( anggota_boyband )
