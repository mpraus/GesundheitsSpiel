import sys, pygame

class Character(pygame.sprite.Sprite):
	def __init__ (self, name, position, imageFile):
		self.name = name
		self.position = position
		self.imageFile = imageFile

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)

	def getCoordinates(self):
		return self.position