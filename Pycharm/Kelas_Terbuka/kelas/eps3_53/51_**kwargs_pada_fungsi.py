""" **kwargs """


def garis():
	print( 30 * '-' )


def fungsi( nama, tinggi, berat ):
	print( f"{nama} punya tinggi {tinggi}, dan berat {berat}" )


fungsi( 'ucup', 180, 70 )
garis()


def fungsi_kwargs( **kwargs ):
	nama = kwargs[ 'nama' ]
	tinggi = kwargs[ 'tinggi' ]
	berat = kwargs[ 'berat' ]
	print( f"{nama} punya tinggi {tinggi}, dan berat {berat}" )


fungsi_kwargs( nama = 'dudung', tinggi = 190, berat = 50 )
