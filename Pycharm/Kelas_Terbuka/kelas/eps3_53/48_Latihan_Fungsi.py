# Latihan Fungsi

# import os

# program menghitung luas dan keliling pesegi panjang

# membuat header program
#
# os.system( "clear" )
# print( f"{'PROGRAM MENGHITUNG LUAS':^40}" )
# print( f"{'DAN KELILING PERSEGI PANJANG':^40}" )
# print( f"{'-' * 40:^40}" )
#
# # mengambil input user
# LEBAR = int( input( "Masukan nilai lebar = " ) )
# PANJANG = int( input( "Masukan nilai panjang = " ) )
#
# # program menghitung luas
# LUAS = PANJANG * LEBAR
# KELILING = 2 * (PANJANG + LEBAR)
#
# # tampilkan hasil
# print( f"hasil perhitungan luas = {LUAS}" )
# print( f"hasil perhitungan keliling = {KELILING}" )

def garis():
	print( 30 * '-' )


def header():
	print( '\n' )
	print( f"{'PROGRAM MENGHITUNG LUAS':^40}" )
	print( f"{'DAN KELILING PERSEGI PANJANG':^40}" )
	print( f"{'-' * 40:^40}" )


def input_user():
	panjang = int( input( "Masukan nilai panjang = " ) )
	lebar = int( input( "Masukan nilai lebar = " ) )

	return lebar, panjang


def hitung_luas():
	luas = PANJANG * LEBAR
	return luas


def hitung_keliling():
	keliling = 2 * (PANJANG + LEBAR)
	return keliling


def hasil_luas():
	print( f"hasil perhitungan luas = {LUAS}" )


# print( f"hasil perhitungan keliling = {KELILING}" )
def hasil_keliling():
	# print( f"hasil perhitungan luas = {LUAS}" )
	print( f"hasil perhitungan keliling = {KELILING}" )


# while True:
# 	header()
# 	LEBAR, PANJANG = input_user()
# 	LUAS = hitung_luas()
# 	KELILING = hitung_keliling()
# 	hasil()
#
# 	isContinue = input( '\nMasih Lanjut (y/n) = ' )
# 	if isContinue == 'n':
# 		break
#
# print( 'Program Selesai, Trimakasih' )


while True:
	header()
	opsi = input( 'ketik 1 untuk hitung luas \nketik 2 untuk hitung keliling \nanda pilih? = ' )
	garis()
	if opsi == '1':
		print( 'Perhitungan Luas' )
		LEBAR, PANJANG = input_user()
		LUAS = hitung_luas()
		hasil_luas()
	else:
		# opsi_2 = input( 'ketik 2 untuk hitung keliling = ' )
		if opsi == '2':
			print( 'Penghitungan Keliling' )
			LEBAR, PANJANG = input_user()
			LUAS = hitung_luas()
			KELILING = hitung_keliling()
			hasil_keliling()

	isContinue = input( '\nMasih Lanjut (y/n) = ' )
	if isContinue == 'n':
		break

print( 'Program Selesai, Trimakasih' )
