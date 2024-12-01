import datetime
import os

mahasiswa_template = \
	{
		'nama': 'nama',
		'nim': '00000000',
		'sks_lulus': 0,
		'lahir': datetime.datetime( 1111, 1, 11 )
	}

data_mahasiswa = { }

print( f"{'SELAMAT DATANG': ^20}" )
print( f"{'DATA MAHASISWA': ^20}" )
print( '-' * 20 )

mahasiswa = dict.fromkeys( mahasiswa_template.keys() )
print( mahasiswa )

mahasiswa[ 'nama' ] = input( 'Nama Mahasiswa = ' )
mahasiswa[ 'nim' ] = input( 'Nim Mahasiswa = ' )
mahasiswa[ 'sks_lulus' ] = int( input( 'SKS Mahasiswa = ' ) )
tahun_lahir = int( input( "Tahun Lahir (YYYY) = " ) )
bulan_lahir = int( input( "Bulan Lahir (MM) = " ) )
tanggal_lahir = int( input( "Tanggal Lahir (DD) = " ) )
mahasiswa[ 'lahir' ] = datetime.datetime( tahun_lahir, bulan_lahir, tanggal_lahir )
print( mahasiswa )
