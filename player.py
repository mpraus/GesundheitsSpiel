import sys, pygame
from character import Character

class Player(Character):

	def __init__ (self, name, x_cord, y_cord, size, imageFile):
		super(Player, self).__init__(name, x_cord, y_cord, size, imageFile)
