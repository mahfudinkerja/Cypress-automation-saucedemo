class Hero:
	def __init__( self, inputName, inputHealth, inputPower, inputArmor ):
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor


hero1 = Hero( 'sniper', 100, 10, 5 )
hero2 = Hero( 'mirana', 100, 15, 3 )
hero3 = Hero( 'gompar', 1000, 100, 0 )

print( hero1.__dict__ )
print( hero2.__dict__ )
print( hero3.__dict__ )