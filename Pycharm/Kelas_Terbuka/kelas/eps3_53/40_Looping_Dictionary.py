# Looping dictionary

friends = {
	'cup': 'ucup surucup',
	'tong': 'otong surotong',
	'dung': 'dudung surudung',
	'sep': 'asep si kasyep',
	'cuy': 'ucuy surucuy'
}

# looping who the key
for friend in friends:
	print( 'looping ', friend )

# operator untuk mengambil item / iterable
print( 20 * '=' )
print( friends.keys() )

print( 20 * '=', "Keys", '=' * 20 )
for key in friends.keys():
	print( 'hasil dari keys :', friends.get( key ) )

print( 20 * '=', "Value", '=' * 20 )
for value in friends.values():
	print( 'hasil dari value : ', value )

print( 20 * '=', "Item", '=' * 20 )
for item in friends.items():
	print( 'hasil dari item : ', item )

print( 20 * '=', "Keys & Values", '=' * 20 )
for key, value in friends.items():
	print( f"key = {key}\t | value = {value}" )
