import sys, pygame
import numpy as np
from character import Character

class Background(pygame.sprite.Sprite):
	def __init__(self, imageFile, levelFile, screenSize):
		pygame.sprite.Sprite.__init__(self)

		levelDoc = open(levelFile)
		mapLine = []
		characterLine = []
		mapDone = False
		for line in levelDoc:
			if line == '\n' or line == '\r\n':
				mapDone = True
			elif mapDone:
				characterLine.append(line.split())
			else:
				mapLine.append(line)

		self.tileMap = np.zeros((len(mapLine[0].split()), len(mapLine))).astype('U256')
		y = 0
		for line in mapLine:
			line = line.split()
			x = 0
			for char in line:
				self.tileMap[x, y] = char
				x+=1
			y+=1

		self.characterArray = []
		for line in characterLine:
			if line[0] == 'player':
				character = Character(line[1], (int(line[2][1]), int(line[2][3])), line[3])
				self.player = character
				self.tileMap[int(line[2][1]), int(line[2][3])] = character
			elif line[0] == 'npc':
				character = Character(line[1], (int(line[2][1]), int(line[2][3])), line[3])
				self.characterArray.append(character)
				self.tileMap[int(line[2][1]), int(line[2][3])] = character
		self.imageFile = imageFile;
		self.calculateMapSize(screenSize)

	def move(self, character, vector):
		newPosition = (character.position[0] + vector[0], character.position[1] + vector[1])
		if self.tileMap[newPosition] == ".":
			self.tileMap[character.position] = "."
			self.tileMap[newPosition] = character.name
			character.position = (newPosition)
			character.rect.left = character.position[0] * self.tileSize
			character.rect.top = character.position[1] * self.tileSize

	def calculateMapSize(self, screenSize):
		mapLengthX = len(self.tileMap)
		mapLengthY = len(self.tileMap[0])

		if screenSize[0] > mapLengthX:
			quotientX = int(screenSize[0] / mapLengthX)
		else:
			quotientX = int(mapLengthX / screenSize[0])
		
		if screenSize[1] > mapLengthY:
			quotientY = int(screenSize[1] / mapLengthY)
		else:
			quotientY = int(mapLengthY / screenSize[1])

		self.tileSize = min(quotientX, quotientY)
		self.mapSize = (mapLengthX * self.tileSize, mapLengthY * self.tileSize)

		self.image = pygame.image.load(self.imageFile)
		self.player.image = pygame.image.load(self.player.imageFile)
		self.player.image = pygame.transform.scale(self.player.image, (self.tileSize, self.tileSize))
		self.rect = pygame.Rect((0, 0), self.mapSize)
		self.player.rect = self.player.image.get_rect()
		self.player.rect.left, self.player.rect.top = self.player.position[0] * self.tileSize, self.player.position[1] * self.tileSize

		for character in self.characterArray:
			character.image = pygame.image.load(character.imageFile)
			character.image = pygame.transform.scale(character.image, (self.tileSize, self.tileSize))
			character.rect = character.image.get_rect()
			character.rect.left, character.rect.top = character.position[0] * self.tileSize, character.position[1] * self.tileSize