import sys, pygame

class Character:

	def __init__ (self, name, position, size, imageFile):
		self.name = name
		self.position = position
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.image = pygame.transform.scale(self.image, self.size)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = self.position