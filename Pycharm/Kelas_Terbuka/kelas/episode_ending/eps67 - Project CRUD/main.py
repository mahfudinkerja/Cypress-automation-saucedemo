import os
import sys

while True:

	if __name__ == '__main__':
		os_name = sys.platform

		if os_name == 'win32':
			os.system( 'cls' )
		elif os_name == 'linux' or os_name == 'darwin':
			os.system( 'clear' )

	print( 'SELAMAT DATANG DI PROGRAM' )
	print( 'DATABASE PERPUSATAKAAN' )
	print( '===========================' )

	print( "1. Read Data" )
	print( "2. Create Data" )
	print( "3. Update Data" )
	print( "4. Delete Data\n" )

	user_option = input( 'Masukan Opsi : ' )
	print( '\n===========================\n' )

	match user_option:
		case "1":
			print( "Read Data" )
		case "2":
			print( "Create Data" )
		case "3":
			print( "Update Data" )
		case "4":
			print( "Delete Data" )

	print( '\n===========================\n' )
	is_done = input( 'Apakah sudah selesai (y/n) ?' )
	if is_done == 'y' or is_done == 'Y':
		break

print( '\nprogram sudah selesai' )
