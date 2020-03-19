import sys, pygame

class Character(pygame.sprite.Sprite):

	# x_cord and y_cord are the position of the character in the map array of the background 
	# size = (height, width) of character
	def __init__ (self, name, x_cord, y_cord, size, imageFile, tileSize):
		self.name = name
		self.x_cord = x_cord
		self.y_cord = y_cord
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.image = pygame.transform.scale(self.image, self.size)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = self.x_cord*tileSize, self.y_cord*tileSize

	def getCoordinates(self):
		return self.x_cord, self.y_cord

