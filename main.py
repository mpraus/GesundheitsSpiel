#! /usr/bin/env python3

import sys, pygame
pygame.init()

black = 0, 0, 0
screen = pygame.display.set_mode()

while(True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	pygame.display.flip()
