#! /usr/bin/env python3

import sys
import pygame
import numpy as np
from background import Background
from player import Player
from character import Character


class Game:

    black = 0, 0, 0
    screenSize = (1366, 768)

    def __init__(self):
        pygame.init()
        mainScreen = pygame.display.set_mode(size=(1024, 768))
        # width, height = mainScreen.get_size()
        width, height = (1024, 768)
        background = Background("images/TestMap.png", "DevMap")
        player = background.player
        arr_x, arr_y = background.map_arr.shape
        objects = background.characterArray.copy()
        objects.append("#")
        while(True):
            player_x, player_y = player.getCoordinates()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    x_cord = player.x_cord
                    y_cord = player.y_cord

                    # movement of player
                    if event.key == pygame.K_UP:
                        if (0 <= y_cord - 1 and
                                background.map_arr[x_cord, y_cord - 1]
                                not in objects):
                            background.move(player, 0, -1, tileSize)
                    if event.key == pygame.K_DOWN:
                        if (y_cord + 1 < arr_y and
                                background.map_arr[x_cord, y_cord + 1] not in
                                objects):
                            background.move(player, 0, 1, tileSize)
                    if event.key == pygame.K_RIGHT:
                        if (x_cord + 1 < arr_x and
                                background.map_arr[x_cord + 1, y_cord] not in
                                objects):
                            background.move(player, 1, 0, tileSize)
                    if event.key == pygame.K_LEFT:
                        if (0 <= x_cord - 1 and
                                background.map_arr[x_cord - 1, y_cord] not in
                                objects):
                            background.move(player, -1, 0, tileSize)
            mainScreen.fill(self.black)
            mainScreen.blit(
                pygame.transform.scale(background.image, (width, height)),
                background.rect)
            mainScreen.blit(player.image, player.rect)
            for npc in background.characterArray:
                mainScreen.blit(npc.image, npc.rect)
            pygame.display.flip()


Game()
