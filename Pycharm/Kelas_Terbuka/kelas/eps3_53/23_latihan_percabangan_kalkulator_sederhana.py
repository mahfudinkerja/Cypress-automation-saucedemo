# # Latihan
#
# # Kalculator
# print(20 * "=")
# print("Kalkulator sederhana")
# print(20 * "=")
#
# angka_1 = float(input("Masukan angka 1 = "))
# operator = input("Operator (+, -, x, /) = ")
# angka_2 = float(input("Masukan angka 2 = "))
#
# # Percabangan
#
# if operator == "+":
#     hasil = angka_1 + angka_2
#     print(f"Hasilnya adalah = {hasil}")
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(f"Hasilnya adalah = {hasil}")
# elif operator == "x" or operator == "*":
#     hasil = angka_1 * angka_2
#     print(f"Hasilnya adalah = {hasil}")
# elif operator == "/":
#     hasil = angka_1 / angka_2
#     print(f"Hasilnya adalah = {hasil}")
# else:
#     print("Masukin yang bener dong operator nya")
#
# print(20*"=")
# print("Program nya selesai")


# # while True:
# while True:
# 	usia = int( input( '\nmasukan umur : ' ) )
#
# 	if usia <= 5:
# 		print( 'anda balita' )
# 	elif 5 <= usia <= 15:
# 		print( 'anda anak anak' )
# 	elif 16 <= usia <= 25:
# 		print( 'anda udah remaja' )
# 	else:
# 		print( 'anda tidak terjangkau fungsi' )
#
# 	is_done = input( '\nudah kelar ? (y/n)' )
# 	if is_done == 'y':
# 		break
#
# print( 'program selesai' )


# saldo_awal = int( input( 'Masukan saldo awal : ' ) )
# deposit = int( input( 'Masukan deposit : ' ) )
# print( 30 * '-' )
# hutang = 10
#
# saldo_akhir = saldo_awal + deposit
# print( f'saldo akhir = {saldo_akhir}' )
#
# if saldo_akhir >= hutang:
# 	print( 'saldo cukup nich buat bayar utang' )
# elif saldo_akhir <= hutang:
# 	print( 'Uang anda tidak cukup' )
#
# bayar_utang = int( input( '\nMasukan nominal yang mau di bayar utang : ' ) )
#
# sisa_hutang = hutang - bayar_utang
# sisa_saldo = saldo_akhir - bayar_utang
#
# print( f'sisa hutang {sisa_hutang}' )
# print( f'sisa saldo = {sisa_saldo}' )

while True:
	saldo_awal = int( input( '\nMasukan saldo awal : ' ) )
	deposit = int( input( 'Masukan deposit : ' ) )
	print( 30 * '-' )
	hutang = 10

	saldo_akhir = saldo_awal + deposit
	print( f'saldo akhir = {saldo_akhir}' )

	if saldo_akhir >= hutang:
		print( 'saldo cukup nich buat bayar utang' )
	elif saldo_akhir <= hutang:
		print( 'Uang anda tidak cukup' )

	bayar_utang = int( input( '\nMasukan nominal yang mau di bayar utang : ' ) )
	sisa_hutang = hutang - bayar_utang
	sisa_saldo = saldo_akhir - bayar_utang

	print( f'sisa hutang {sisa_hutang}' )
	print( f'sisa saldo = {sisa_saldo}' )

	is_done = input( '\nlanjut ga ? (y/n)' )
	if is_done == 'n':
		break
print( 'program selesai' )
#
