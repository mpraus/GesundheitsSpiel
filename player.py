import sys
import pygame
from character import Character


class Player(Character):

    def __init__(self, name, position, imageFile):
        super(Player, self).__init__(name, position, imageFile)
