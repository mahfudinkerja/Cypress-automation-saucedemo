# membaca file external
from garis import garis

print( 5 * '_', 'Membaca file External', '_' * 5 )
file = open( 'data.txt', mode = 'r' )

print( f"status read : {file.readable()}" )
print( f"status write : {file.writable()}" )
# print( f"file didalam data.txt = \n{file.read()}" )
garis()

# baca perbaris
# print( file.readline(),end ='' )
# print( file.readline(),end = '' )
# print( file.readline( 5 ) )

# baca semua baris sebagai list
print( file.readlines() )

print( f"apakah file sudah di close ? : {file.closed}" )
file.close()
print( f"apakah file sudah di close ? : {file.closed}" )

garis()
print( '\n', 5 * '_', 'Membaca file External', '_' * 5 )

with open( 'data.txt', mode = 'r' ) as file:
	content = file.readline()
	print( content, end = '' )
	print( f"apakah file sudah di close : {file.closed}" )

print( f"apakah file sudah di close : {file.closed}" )
