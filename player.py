import sys, pygame
from character import Character

class Player(Character):

	def __init__ (self, name, position, size, imageFile):
		super(Player, self).__init__(name, position, size, imageFile)
		