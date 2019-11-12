import sys, pygame
import numpy as np

class Background(pygame.sprite.Sprite):

	def __init__(self, imageFile, height, width, tileSize):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = [0,0]
		self.map_arr = np.zeros((int(round(width / 50)), int(round(height / 50)))).astype('U256')
		self.tileSize = tileSize