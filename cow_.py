import pygame
import random
from main_game import Object


class Cow(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)
        self.speed = 2
        self.change_direction_time = 0
        self.dx, self.dy = 0, 0 
        self.state = 0


    def update(self, walls, board):
        if pygame.time.get_ticks() > self.change_direction_time:
            self.dx = random.choice([-1, 0, 1])
            self.dy = random.choice([-1, 0, 1])
            self.change_direction_time = pygame.time.get_ticks() + random.randint(1000, 2000)

        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        if self.rect.left < board.rect.left or self.rect.right > board.rect.right:
            self.dx *= -1
        if self.rect.top < board.rect.top or self.rect.bottom > board.rect.bottom:
            self.dy *= -1

        board.keep_inside(self.rect)

        for wall in walls:
            if self.rect.colliderect(wall.rect):

                self.rect.x -= self.dx * self.speed
                self.rect.y -= self.dy * self.speed
                self.dx *= -1
                self.dy *= -1
