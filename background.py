import sys, pygame

class Background(pygame.sprite.Sprite):

	def __init__(self, imageFile):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = [0,0]