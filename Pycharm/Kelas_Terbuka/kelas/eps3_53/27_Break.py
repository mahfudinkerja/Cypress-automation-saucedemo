angka = 3
while angka < 5:
	angka += 1
	print( f"Count = ", angka )

	if angka == 3:
		print( "Nice" )
		break
	print( "Wasuupp!" )
print( "program finish" )

# contoh ke 2
data_int = str( input( "\nHitung sampai = " ) )
angka = 0
while True:
	angka += 1
	print( f"Count = ", angka )

	if angka == data_int:
		print( "Nice" )
		break
	print( "Wasuupp!" )
print( "program finish" )
