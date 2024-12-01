from matematika_55 import tambah, kali, pangkat

print( f"Hasil tambah = {tambah( 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 )}" )
print( f"Hasil kali = {kali( 1, 2, 3, 4, 5, 4, 3, 2, 1 )}" )
print( f"Hasil Pangkat3 = {pangkat( 5 )( 5 )}" )

# membuat alias


print( 30 * '-' )
from matematika_55 import tambah as add
from matematika_55 import kali as dikali
from matematika_55 import pangkat as pangkuy

print( f"Hasil tambah = {add( 1, 2, 3, 4, 4, 5, 3, 2, 3, 4 )}" )
print( f"Hasil kali = {dikali( 1, 2, 3, 4, 2, 1 )}" )
print( f"Hasil Pangkat3 = {pangkuy( 5 )( 5 )}" )
