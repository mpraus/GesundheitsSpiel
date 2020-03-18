import sys, pygame
import numpy as np

class Background(pygame.sprite.Sprite):

	def __init__(self, imageFile, mapFile):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = [0,0]
		self.loadLevel(mapFile)


	def loadLevel(self, filename):
		levelDoc = open(filename)
		mapLine = []
		characterLine = []
		i = 0
		mapDone = False
		for line in levelDoc:
			if line == '\n' or line == '\r\n':
				mapDone = True
			if mapDone:
				characterLine.append(line.split())
			else:
				mapLine.append(line)

		self.map_arr = np.zeros((len(mapLine[0].split()), len(mapLine))).astype('U256')
		i = 0
		for line in mapLine:
			line = line.split()
			j = 0
			for char in line:
				self.map_arr[j,i] = line[j]
				j+=1
			i+=1
		print(characterLine)