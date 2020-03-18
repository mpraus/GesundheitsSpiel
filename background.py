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


	def move(self, character, x, y, tileSize):
		self.map_arr[character.x_cord, character.y_cord] = "."
		character.x_cord += x
		character.y_cord += y
		self.map_arr[character.x_cord, character.y_cord] = character.name
		character.rect.left = character.x_cord * tileSize
		character.rect.top = character.y_cord * tileSize


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

		self.map_arr = np.zeros((len(mapLine[0].split()), len(mapLine))).astype('U256')
		i = 0
		for line in mapLine:
			line = line.split()
			j = 0
			for char in line:
				self.map_arr[j,i] = line[j]
				j+=1
			i+=1

		self.characterArray = []
		for line in characterLine:
			if line[0] == 'player':
				character = Character(line[1], int(line[2][1]), int(line[2][3]), (self.TILESIZE,self.TILESIZE), line[3], self.TILESIZE)
				self.player = character
				self.map_arr[int(line[2][1]), int(line[2][3])] = character
			elif line[0] == 'npc':
				#needs to be changed once we know what we're going to do with npcs
				character = Character(line[1], int(line[2][1]), int(line[2][3]), (self.TILESIZE,self.TILESIZE), line[3], self.TILESIZE)
				self.characterArray.append(character)
				self.map_arr[int(line[2][1]), int(line[2][3])] = character