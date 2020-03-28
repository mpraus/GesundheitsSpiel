import sys, pygame
import numpy as np
from background import Background
from player import Player
from character import Character

class Game:
	def __init__(self):
		BLACK = 0, 0, 0
		screenSize = (1024, 768)

		pygame.init()
		mainScreen = pygame.display.set_mode(screenSize)
		background = Background("images/TestMap.png", "DevMap", screenSize)
		player = background.player
		tilesX, tilesY = background.tileMap.shape

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					playerX, playerY = player.position
					if event.key == pygame.K_UP:
						if 0 <= playerY - 1: background.move(player, (0, -1))
					if event.key == pygame.K_DOWN:
						if playerY + 1 < tilesY: background.move(player, (0, 1))
					if event.key == pygame.K_RIGHT:
						if playerX + 1 < tilesX: background.move(player, (1, 0))
					if event.key == pygame.K_LEFT:
						if 0 <= playerX - 1: background.move(player, (-1, 0))
			
			mainScreen.fill(BLACK)
			mainScreen.blit(pygame.transform.scale(background.image, screenSize), background.rect)
			mainScreen.blit(player.image, player.rect)
			for npc in background.characterArray:
				mainScreen.blit(npc.image, npc.rect)
			
			pygame.display.flip()
	
Game()