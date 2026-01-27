import pygame
import random
from object import *
from statemachine import StateMachine
import cow_statemachine

class Cow(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color,game)
        self.image = pygame.image.load("AnimalProtectionGame/image/cow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (sx, sy))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.speed = 2
        self.change_direction_time = 0
        self.dx, self.dy = 0, 0 

        self.state_machine = StateMachine(self)
        


    def update(self, walls, board):
        
        if not self.state_machine.current_state:
            self.change_state(cow_statemachine.Idle(self))
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
        
        for box in self.game.boxes:

            if self.rect.colliderect(box.rect):
                # cow uses self.dx/self.dy; convert to pixel deltas for Box.push
                push_dx = int(self.dx * self.speed)
                push_dy = int(self.dy * self.speed)

                if box.push(push_dx, push_dy, walls):
                    # push succeeded: bounce cow away
                    self.dx *= -1
                    self.dy *= -1
                    self.rect.x += int(self.dx * self.speed)
                    self.rect.y += int(self.dy * self.speed)
                else:
                    # push failed: block cow and reverse
                    if push_dx > 0:
                        self.rect.right = box.rect.left
                    if push_dx < 0:
                        self.rect.left = box.rect.right
                    if push_dy > 0:
                        self.rect.bottom = box.rect.top
                    if push_dy < 0:
                        self.rect.top = box.rect.bottom

                    self.dx *= -1
                    self.dy *= -1

        

    def change_state(self, state):
        self.state_machine.change_state(state)