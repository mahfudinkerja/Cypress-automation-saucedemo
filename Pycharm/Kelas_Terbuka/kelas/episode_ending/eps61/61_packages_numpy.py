import numpy as np


def garis():
	print( 30 * '-' )


list_a = [ 1, 2, 3, 4 ]
vector_a = np.array( [ 6, 7, 8, 9, 10 ] )

print( f"list_a = {list_a}" )
print( f"vertor_a = {vector_a}" )
print( f"vertor_a pangkat 2 = {vector_a ** 2}" )
print( f"vertor_a kali 5 = {vector_a * 5}" )

garis()
matrix_b = np.array( [ (1, 2), (4, 5) ] )
print( f"matrix b =\n{matrix_b}" )
garis()

zeros_c = np.zeros( (2, 2) )
print( f"zeros c = \n{zeros_c}" )
garis()

ones_d = np.ones( (2, 2) )
print( f"Ones D = \n{ones_d}" )

garis()

jumlah = matrix_b + matrix_b ** 2 + ones_d
print( f"Jumlah = \n{jumlah}" )
