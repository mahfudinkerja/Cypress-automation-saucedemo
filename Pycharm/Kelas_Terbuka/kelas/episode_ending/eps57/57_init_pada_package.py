import sains.matematika as mtk
import sains.fisika as fisika

# import sains.matematika as mtk
#  => hasil_tambah = mtk.tambah (....)

hasil_tambah = mtk.tambah( 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9 )
print( f"hasil tambah = {hasil_tambah}" )

hasil_kali = mtk.kali( 1, 2, 5, 6, 7, 8 )
print( f"hasil kali = {hasil_kali}" )

pangkat_3 = mtk.pangkat( 3 )
print( f"hasil pangkat 3 = {pangkat_3( 5 )}" )

hasil_fisika = fisika.gaya( 10, 9.9 )
print( f"hasil gaya = {hasil_fisika}" )
