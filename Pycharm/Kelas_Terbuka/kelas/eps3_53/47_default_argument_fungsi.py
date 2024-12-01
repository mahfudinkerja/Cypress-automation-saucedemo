"""Defaul Argument"""


def garis():
	print( 40 * '-' )


def say_hi( nama = 'Ganteng' ):
	print( f"Hallo {nama}" )


say_hi( 'ucup' )
say_hi()
garis()


def sapa_dia( nama, pesan = 'Apa kabar?' ):
	print( f"hai {nama}, {pesan}" )


sapa_dia( 'ucup', 'Kamu ganteng' )
sapa_dia( 'ucup', )

garis()


def hitung_pangkat( angka, pangkat ):
	hasil = angka ** pangkat
	return hasil


print( hitung_pangkat( 2, 4 ) )
print( hitung_pangkat( pangkat = 2, angka = 5 ) )

garis()


def fungsi( input1 = 1, input2 = 2, input3 = 3, input4 = 4 ):
	hasil = input1 + input2 + input3 + input4
	return hasil


print( fungsi() )
print( fungsi( input4 = 14 ) )
