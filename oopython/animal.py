# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"This animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat")
		self.toy = toy
		self.breed = breed
	def play(self):
		print(f"{self.name} plays with {self.toy}!")



blue = Cat("Blue","Scottish Fold", "String")
blue.play()


# OUR "MODEL" FOR AN ANIMAL AND the subclass called CAT
# Animal
# 	species
# 	name

# Cat
# 	species
# 	name
# 	breed
# 	favorite_toy