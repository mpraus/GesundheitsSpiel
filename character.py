import sys, pygame

class Character(pygame.sprite.Sprite):
	def __init__ (self, name, position, size, imageFile):
		self.name = name
		self.position = position
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.image = pygame.transform.scale(self.image, (self.size, self.size))
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = self.position[0]*size, self.position[1]*size

	def getCoordinates(self):
		return self.position