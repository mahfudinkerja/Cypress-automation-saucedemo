def garis():
	print( 30 * '-' )


import datetime

data_waktu = datetime.datetime.now()
print( f"datetime now : {data_waktu}" )
print( f"tahun now : {data_waktu.year}" )
print( f"date format %A : {data_waktu.strftime( '%A' )}" )
# print( f"date format %B : {data_waktu.strftime( '%B' )}" )
# print( f"date format %C : {data_waktu.strftime( '%C' )}" )
# print( f"date format %E : {data_waktu.strftime( '%E' )}" )
# print( f"date format %F : {data_waktu.strftime( '%F' )}" )
# print( f"date format %G : {data_waktu.strftime( '%G' )}" )
# print( f"date format %H : {data_waktu.strftime( '%H' )}" )
# print( f"date format %H : {data_waktu.strftime( '%H' )}" )
# print( f"date format %I : {data_waktu.strftime( '%I' )}" )
# print( f"date format %J : {data_waktu.strftime( '%J' )}" )
# print( f"date format %K : {data_waktu.strftime( '%K' )}" )
# print( f"date format %L : {data_waktu.strftime( '%L' )}" )
# print( f"date format %M : {data_waktu.strftime( '%M' )}" )
# print( f"date format %N : {data_waktu.strftime( '%N' )}" )
# print( f"date format %O : {data_waktu.strftime( '%O' )}" )
# print( f"date format %P : {data_waktu.strftime( '%P' )}" )
# print( f"date format %Q : {data_waktu.strftime( '%Q' )}" )
# print( f"date format %R : {data_waktu.strftime( '%R' )}" )
# print( f"date format %S : {data_waktu.strftime( '%S' )}" )
# print( f"date format %T : {data_waktu.strftime( '%T' )}" )
# print( f"date format %U : {data_waktu.strftime( '%U' )}" )
# print( f"date format %V : {data_waktu.strftime( '%V' )}" )
# print( f"date format %W : {data_waktu.strftime( '%W' )}" )
# print( f"date format %X : {data_waktu.strftime( '%X' )}" )
# print( f"date format %Y : {data_waktu.strftime( '%Y' )}" )
# print( f"date format %Z : {data_waktu.strftime( '%Z' )}" )
from collections import Counter

garis()

data = [ 'q', 23, 'm', 67, 'b', 12, 'd', 45, 'r', 89, 's', 3, 'a', 58, 'y', 22, 'j', 76, 'u', 94, 'e', 1, 'n', 37,
         't', 80, 'x', 50, 'p', 9, 'f', 64, 'z', 30, 'l', 17, 'o', 72, 'c', 41, 'k', 8, 'v', 99, 'g', 6, 'i', 27, 'w',
         84, 'h', 56,
         'a', 39, 'e', 4, 'n', 92, 'p', 15, 's', 70, 'm', 33, 'o', 88, 'x', 21, 'r', 53, 'i', 98, 'f', 11, 'v', 61, 't',
         35, 'z', 90, 'y', 5, 'b', 26, 'c', 83, 'd', 47, 'u', 74, 'w', 16, 'l', 62, 'q', 38, 'j', 95, 'k', 2, 'g', 31,
         'h',
         55, 'v', 87, 'e', 13, 'i', 68, 'z', 7, 'o', 19, 'n', 44, 't', 79, 'f', 20, 's', 66, 'm', 10, 'd', 59, 'u', 81,
         'k', 42, 'p', 28, 'q', 63, 'j', 93, 'y', 18, 'x', 77, 'r', 34, 'b', 54, 'c', 85, 'a', 32, 'w', 14, 'g', 71,
         'h',
         46, 'l', 60, 'v', 25, 'o', 96, 'n', 40, 'e', 29, 't', 86, 's', 57, 'm', 73, 'i', 24, 'f', 78, 'x', 52, 'z', 48,
         'p', 69, 'j', 36, 'k', 65, 'y', 97, 'r', 43, 'u', 75, 'b', 91, 'q', 49, 'w', 82, 'g', 0, 'h', 88, 13 ]

data_count = Counter( data )
print( f"data count = {data_count}" )
print( f"data count = {data_count[ 'a' ]}" )
print( f"data count = {data_count[ 13 ]}" )

garis()

import io

file = io.open( 'file_text.txt', 'r' )
print( file.read() )
