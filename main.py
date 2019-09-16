#! /usr/bin/env python3

import sys, pygame
class MainScreen:

	black = 0, 0, 0

	def __init__(self):
		pygame.init()

		mainScreen = pygame.display.set_mode()

		while(True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()

			mainScreen.fill(black)
			pygame.display.flip()
