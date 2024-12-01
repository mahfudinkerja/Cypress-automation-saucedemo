import os
import sys

import CRUD as CRUD


def garis():
	print( '\n===========================\n' )


if __name__ == '__main__':
	os_name = sys.platform

	if os_name == 'win32':
		os.system( 'cls' )
	elif os_name == 'linux' or os_name == 'darwin':
		os.system( 'clear' )

print( 'SELAMAT DATANG DI PROGRAM' )
print( 'DATABASE PERPUSATAKAAN' )
garis()

CRUD.init_console()

while True:

	if __name__ == '__main__':
		os_name = sys.platform

		if os_name == 'win32':
			os.system( 'cls' )
		elif os_name == 'linux' or os_name == 'darwin':
			os.system( 'clear' )

	print( 'SELAMAT DATANG DI PROGRAM' )
	print( 'DATABASE PERPUSATAKAAN' )
	garis()
	print( "1. Read Data" )
	print( "2. Create Data" )
	print( "3. Update Data" )
	print( "4. Delete Data\n" )

	user_option = input( 'Masukan Opsi : ' )
	# garis()
	match user_option:
		case "1":
			CRUD.read_console()
		case "2":
			print( "Create Data" )
		case "3":
			print( "Update Data" )
		case "4":
			print( "Delete Data" )

	# garis()
	is_done = input( 'Apakah sudah selesai (y/n) ?' )
	if is_done == 'y' or is_done == 'Y':
		break

print( '\nprogram sudah selesai' )
