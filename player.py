import sys, pygame
from character import Character

class Player(Character):

	def __init__ (self, name, x_cord, y_cord, size, imageFile):
		super(Player, self).__init__(name, x_cord, y_cord, size, imageFile)

	def move(self, x, y):
		self.x_cord += x
		self.y_cord += y
		self.rect.left = self.x_cord
		self.rect.top = self.y_cord