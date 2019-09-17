#! /usr/bin/env python3

import sys, pygame

class Game:

	black = 0, 0, 0

	def __init__(self):
		pygame.init()

		mainScreen = pygame.display.set_mode()

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			mainScreen.fill(self.black)
			pygame.display.flip()
            
Game()