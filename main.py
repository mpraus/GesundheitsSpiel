#! /usr/bin/env python3

import sys, pygame
import numpy as np
from background import Background
from player import Player
from character import Character

class Game:

	black = 0, 0, 0
	screenSize = (1366,768)

	def move(self, character, x, y, tileSize, background):
		background.map_arr[character.x_cord, character.y_cord] = 0
		character.x_cord += x
		character.y_cord += y
		background.map_arr[character.x_cord, character.y_cord] = character.name
		character.rect.left = character.x_cord * tileSize
		character.rect.top = character.y_cord * tileSize

	def __init__(self):
		pygame.init()

		mainScreen = pygame.display.set_mode(size=self.screenSize)
		width, height = mainScreen.get_size()
		tileSize = 50
		background = Background("images/background_example.png", height, width,tileSize)
		player = Player("Player1", 0, 0, (background.tileSize, background.tileSize), "images/harpy.png")
		computerPlayer1 = Character("Computer1", 7*50, 6*50, (background.tileSize, background.tileSize), "images/minotaur.png")
		background.map_arr[0,0] = player.name
		background.map_arr[7,6] = computerPlayer1.name
		arr_x, arr_y = background.map_arr.shape
		objects = (player.name, computerPlayer1.name)
		
		while(True):
			player_x, player_y = player.getCoordinates()
			for event in pygame.event.get():
				if event.type == pygame.QUIT: sys.exit()
				if event.type == pygame.KEYDOWN:
					x_cord = player.x_cord
					y_cord = player.y_cord


					#movement of player
					if event.key == pygame.K_UP:
						if 0 <= y_cord - 1 < arr_y and background.map_arr[x_cord, y_cord - 1] not in objects:
							self.move(player, 0, -1, tileSize, background)
					if event.key == pygame.K_DOWN:
						if 0 <= y_cord + 2 < arr_y and background.map_arr[x_cord, y_cord + 1] not in objects:
							self.move(player, 0, 1, tileSize, background)
					if event.key == pygame.K_RIGHT:
						if 0 <= x_cord + 1 < arr_x and background.map_arr[x_cord + 1, y_cord] not in objects:
							self.move(player, 1, 0, tileSize, background)
					if event.key == pygame.K_LEFT:
						if 0 <= x_cord - 1 < arr_x and background.map_arr[x_cord - 1, y_cord] not in objects:
							self.move(player, -1, 0, tileSize, background)

			mainScreen.fill(self.black)
			mainScreen.blit(pygame.transform.scale(background.image, self.screenSize), background.rect)
			mainScreen.blit(player.image, player.rect)
			mainScreen.blit(computerPlayer1.image, computerPlayer1.rect)
			pygame.display.flip()
			
Game()