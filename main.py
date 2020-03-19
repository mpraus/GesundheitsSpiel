import sys, pygame
import numpy as np
from background import Background
from player import Player
from character import Character

class Game:
	BLACK = 0, 0, 0

	def __init__(self):
		screenSize = (1024, 768)

		pygame.init()
		mainScreen = pygame.display.set_mode(screenSize)
		background = Background("images/TestMap.png", "DevMap")
		player = background.player
		tilesX, tilesY = background.tileMap.shape
		gameObjects = background.characterArray.copy()
		gameObjects.append("#")

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					playerX = player.position[0]
					playerY = player.position[1]
					
					if event.key == pygame.K_UP:
						if 0 <= playerY - 1 and background.tileMap[playerX, playerY - 1] not in gameObjects:
							background.move(player, 0, -1)
					if event.key == pygame.K_DOWN:
						if playerY + 1 < tilesY and background.tileMap[playerX, playerY + 1] not in gameObjects:
							background.move(player, 0, 1)
					if event.key == pygame.K_RIGHT:
						if playerX + 1 < tilesX and background.tileMap[playerX + 1, playerY] not in gameObjects:
							background.move(player, 1, 0)
					if event.key == pygame.K_LEFT:
						if 0 <= playerX - 1  and background.tileMap[playerX - 1, playerY] not in gameObjects:
							background.move(player, -1, 0)
			
			mainScreen.fill(self.BLACK)
			mainScreen.blit(pygame.transform.scale(background.image, screenSize), background.rect)
			mainScreen.blit(player.image, player.rect)
			for npc in background.characterArray:
				mainScreen.blit(npc.image, npc.rect)
			
			pygame.display.flip()
	
Game()