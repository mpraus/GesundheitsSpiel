#! /usr/bin/env python3

import sys, pygame
import numpy as np
from background import Background
from player import Player
from character import Character

class Game:

	black = 0, 0, 0
	screenSize = (1366,768)

	def __init__(self):
		pygame.init()

		mainScreen = pygame.display.set_mode(size=self.screenSize)
		width, height = mainScreen.get_size()
		tileSize = 50
		background = Background("images/background_example.png", height, width,tileSize)
		player = Player("Player1", 0, 0, (50, 50), "images/harpy.png")
		background.map_arr[0,0] = player.name

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					x_cord = player.x_cord
					y_cord = player.y_cord
					if event.key == pygame.K_UP:
						if 0 <= y_cord - tileSize :
							player.move(0,-1, tileSize)
					if event.key == pygame.K_DOWN:
						if 0 <= y_cord + tileSize * 2 <= height - tileSize:
							player.move(0,1, tileSize)
					if event.key == pygame.K_RIGHT:
						if 0 <= x_cord + tileSize <= width - tileSize:
							player.move(1,0, tileSize)
					if event.key == pygame.K_LEFT:
						if 0 <= x_cord - tileSize:
							player.move(-1,0, tileSize)
				

			mainScreen.fill(self.black)
			mainScreen.blit(pygame.transform.scale(background.image, self.screenSize), background.rect)
			mainScreen.blit(player.image, player.rect)
			pygame.display.flip()
            
Game()