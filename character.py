import sys, pygame

class Character(pygame.sprite.Sprite):

	def __init__ (self, name, x_cord, y_cord, size, imageFile):
		self.name = name
		self.x_cord = x_cord
		self.y_cord = y_cord
		self.size = size

		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.image = pygame.transform.scale(self.image, self.size)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = self.x_cord, self.y_cord
		
	def get_y_cord(self):
		return self.y_cord

	def get_x_cord(self):
		return self.x_cord

	def get_size(self):
		return self.size