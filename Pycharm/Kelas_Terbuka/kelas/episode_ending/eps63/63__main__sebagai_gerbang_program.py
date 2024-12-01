# __main__ adalah top level code enviroment

# __name__ == '__main__'

# __name__ pada file program utama
print( f"nilai __name__ pada main.py = {__name__}" )

# __name__ pada file external
import fungsi


# deklarasi
def fungsi_tambah( a, b ) -> int:
	return a + b


# fungsi utama
if __name__ == '__main__':
	angka1 = 5
	angka2 = 10
	hasil = fungsi_tambah( angka1, angka2 )
	print( f"hasil tambah = {hasil}" )
