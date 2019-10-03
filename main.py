#! /usr/bin/env python3

import sys, pygame
from background import Background
from player import Player
from character import Character

class Game:

	black = 0, 0, 0
	screenSize = (1920,1080)

	def __init__(self):
		pygame.init()

		mainScreen = pygame.display.set_mode(size=self.screenSize)
		background = Background("images/background_example.png")
		player = Player("Player1", [50,50], [100, 150], "images/harpy.png")

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			mainScreen.fill(self.black)
			mainScreen.blit(pygame.transform.scale(background.image, self.screenSize), background.rect)
			mainScreen.blit(player.image, player.rect)
			pygame.display.flip()
            
Game()