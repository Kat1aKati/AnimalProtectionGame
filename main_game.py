import pygame
import random
import time
import math
from statemachine import StateMachine

import world
from board import Board
from player import Player
from object import Object, Wall, Box, Wheat, Tile, Door
from cow import Cow

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
        pygame.display.set_caption("game")
        self.clock = pygame.time.Clock()
        self.running = True

        self.setup()

    def setup(self):
        # move ALL object creation here
        #maybe later
        self.boxes = []
        self.tiles = []

        self.player = Player(250, 250, pygame.Color("#2200FE"), self)
        self.board = Board(10, 10)
        self.cow = Cow(200, 350, 49, 40, pygame.Color("#FFFFFF"), self)

        self.walls = [
            Wall(400, 50, 40, 400, pygame.Color("#474747"), self),
            Wall(400, 700, 1080, 40, pygame.Color("#474747"), self),
            Wall(1100, 250, 40, 450, pygame.Color("#474747"), self)
        ]

        self.boxes.append(Box(200, 550, 50, 50, pygame.Color("#783E00"), self))
        self.boxes.append(Box(500, 200, 50, 50, pygame.Color("#783E00"), self))

        self.tiles.append(Tile(500, 500, 75, 75, pygame.Color("#00FF00"), self))

        self.door = Door(300, 350, 100, 50, pygame.Color("#FF0095"), self)
        self.wheat = Wheat(150, 100, 10, 10, pygame.Color("#D3BE00"), self)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.move(keys, self.board)
        self.cow.update(self.walls, self.board)
        self.door.shift_doors()

        if self.player.rect.colliderect(self.wheat.rect):
            self.wheat.picked_up = True

        for tile in self.tiles:
            colliding = tile.rect.collidelist(self.boxes) != -1

            if colliding and not tile.was_activated:
                tile.activate_tile()

            if not colliding and tile.was_activated:
                tile.activate_tile()

            tile.was_activated = colliding

        self.cow.state_machine.update()


    def render(self):
        self.screen.fill("black")

        self.screen.blit(self.board.image, self.board.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.cow.image, self.cow.rect)
        self.screen.blit(self.wheat.image, self.wheat.rect)

        for wall in self.walls:
            self.screen.blit(wall.image, wall.rect)

        for box in self.boxes:
            self.screen.blit(box.image, box.rect)

        for tile in self.tiles:
            self.screen.blit(tile.image, tile.rect)

        if self.door.opened:
            self.screen.blit(self.door.image, self.door.rect)

        pygame.display.flip()

if __name__ == "__main__":
    Game().run()