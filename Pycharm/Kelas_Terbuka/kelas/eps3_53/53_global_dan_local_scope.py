# global dan local scope

def garis():
	print( 30 * '-' )


nama_global = 'otong'


# akses variable global dengan fungsi
def fungsi1():
	print( f"fungsi menampilkan {nama_global}" )


fungsi1()

# akses varibale global dalam loop
for i in range( 0, 10 ):
	print( f" loop {i} - {nama_global}" )

# percabangan
if True:
	print( f"if menampilkan {nama_global}" )

garis()


# variable local scope
def fungsi2():
	nama_local = 'ucup'


fungsi2()


# contoh 1, penggunaan
def say_otong():
	print( f"hello {nama}" )


nama = 'Otong'
say_otong()
garis()
# contoh 2, merubah varibal global

angka = 15
name = 'ucup'


def ubah( nilai_baru, nama_baru ):
	global angka
	global name
	angka = nilai_baru
	name = nama_baru


print( f"sebelum {angka, name}" )
ubah( 10, 'dudung' )
print( f"sesudah {angka, name}" )
garis()
# contoh 3,

angka = 0

for i in range( 0, 20 ):
	angka += i
	angka_dummy = 0

print( angka )
print( angka_dummy )
garis()

if True:
	angka = 10
	angka_dummy = 20

print( angka )
print( angka_dummy )
