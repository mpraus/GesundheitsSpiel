import sys, pygame
import numpy as np
from character import Character

class Background(pygame.sprite.Sprite):
	TILESIZE = 64

	def __init__(self, imageFile, mapFile):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(imageFile)
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = [0,0]
		self.loadLevel(mapFile)

	def move(self, character, vector):
		newPosition = (character.position[0] + vector[0], character.position[1] + vector[1])
		if self.tileMap[newPosition] == ".":
			self.tileMap[character.position] = "."
			self.tileMap[newPosition] = character.name
			character.position = (newPosition)
			character.rect.left = character.position[0] * self.TILESIZE
			character.rect.top = character.position[1] * self.TILESIZE

	def loadLevel(self, filename):
		levelDoc = open(filename)
		mapLine = []
		characterLine = []
		i = 0
		mapDone = False
		for line in levelDoc:
			if line == '\n' or line == '\r\n':
				mapDone = True
			elif mapDone:
				characterLine.append(line.split())
			else:
				mapLine.append(line)

		self.tileMap = np.zeros((len(mapLine[0].split()), len(mapLine))).astype('U256')
		i = 0
		for line in mapLine:
			line = line.split()
			j = 0
			for char in line:
				self.tileMap[j,i] = line[j]
				j+=1
			i+=1

		self.characterArray = []
		for line in characterLine:
			if line[0] == 'player':
				character = Character(line[1], (int(line[2][1]), int(line[2][3])), self.TILESIZE, line[3])
				self.player = character
				self.tileMap[int(line[2][1]), int(line[2][3])] = character
			elif line[0] == 'npc':
				character = Character(line[1], (int(line[2][1]), int(line[2][3])), self.TILESIZE, line[3])
				self.characterArray.append(character)
				self.tileMap[int(line[2][1]), int(line[2][3])] = character