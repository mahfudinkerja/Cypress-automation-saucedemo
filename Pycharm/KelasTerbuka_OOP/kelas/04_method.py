class Hero:
	# class varibale
	jumlah_hero = 0

	def __init__( self, inputName, inputHealth, inputPower, inputArmor ):
		# instance varibale
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

	# void function, method tanpa return
	def siapa( self ):
		print( f"Namaku adalah {self.name}" )

	# # method dengan argument tanpa return
	def helathUp( self, up ):
		self.health += up

	# method dengan retun
	def getHealth( self ):
		return self.health


hero1 = Hero( 'sniper', 100, 10, 5 )
hero2 = Hero( 'mario bros', 90, 5, 10 )

hero1.siapa()
hero1.helathUp( 10 )

print( hero1.health )
