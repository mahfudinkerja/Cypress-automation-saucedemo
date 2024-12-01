class Hero:
	jumlah = 0

	def __init__( self, inputName, inputHealth, inputPower, inputArmor ):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor

		Hero.jumlah += 1
		print( 'membuat hero dengan nama', inputName )
		print( 'membuat hero dengan health', inputHealth )
		print( 'membuat hero dengan power', inputPower )
		print( 'membuat hero dengan armor', inputArmor )


hero1 = Hero( 'sniper', 100, 10, 5 )
print( Hero.jumlah )
hero2 = Hero( 'mirana', 100, 15, 3 )
print( Hero.jumlah )
hero3 = Hero( 'gompar', 1000, 100, 0 )
print( Hero.jumlah )
