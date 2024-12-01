"""Fungsi dari kembalian"""


def garis():
	print( 30 * '-' )


# template
# def nama_fungsi(argument):
# 	badan fungsi
# 	return output


def kuadrat( input_angka ):
	output_angka = input_angka ** 2
	return output_angka


y = kuadrat( 5 )
print( f"hasil kuadrat y = {y}" )
garis()
print( kuadrat( 8 ) )

z = 1 + kuadrat( 8 )
print( z )

garis()


def fungsi_tambah( angka_1, angka_2 ):
	return angka_1 + angka_2


a = fungsi_tambah( 10, 2 )
print( a )

garis()


def operasi_matematika( angka_1, angka_2 ):
	tambah = angka_1 + angka_2
	kurang = angka_1 - angka_2
	kali = angka_1 * angka_2
	bagi = angka_1 / angka_2

	return tambah, kurang, kali, bagi


k, l, m, n = operasi_matematika( 10, 2 )

print( f"Hasil tambah = {k}" )
print( f"Hasil kurang = {l}" )
print( f"Hasil kali = {m}" )
print( f"Hasil bagi = {n}" )
