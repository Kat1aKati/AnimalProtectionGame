import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
pygame.display.set_caption("game")
clock = pygame.time.Clock()

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(0, 0, 255)):
        super().__init__()
        self.image = pygame.Surface((1480, 780)) #subject to change
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = color
        self.x = x
        self.y = y

    def keep_inside(self, rect):
        if rect.left < self.rect.left:
            rect.left = self.rect.left
        if rect.right > self.rect.right:
            rect.right = self.rect.right
        if rect.top < self.rect.top:
            rect.top = self.rect.top
        if rect.bottom > self.rect.bottom:
            rect.bottom = self.rect.bottom

class Player():
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((75, 75))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = color
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, keys, walls, box, board):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        self.rect.x += dx
        self.handle_collisions(walls, box, dx, 0)
        self.rect.y += dy
        self.handle_collisions(walls, box, 0, dy)

        board.keep_inside(self.rect)

    def handle_collisions(self, walls, box, dx, dy):

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

        if self.rect.colliderect(box.rect):

            if box.push(dx, dy, walls):
                pass 
            else:

                if dx > 0:
                    self.rect.right = box.rect.left
                if dx < 0:
                    self.rect.left = box.rect.right
                if dy > 0:
                    self.rect.bottom = box.rect.top
                if dy < 0:
                    self.rect.top = box.rect.bottom

class Object():
    def __init__(self, x, y, sx, sy, color):
        super().__init__()
        self.image = pygame.Surface((sx, sy))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = color
        self.x = x
        self.y = y

class Wall(Object):
    def __init__(self, x, y,  sx, sy, color):
        super().__init__(x, y, sx, sy, color)

class Cow(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)
        self.speed = 2
        self.change_direction_time = 0
        self.dx, self.dy = 0, 0 

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


class Box(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)

    def push(self, dx, dy, walls):
        self.rect.x += dx
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right

        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

        board.keep_inside(self.rect)

player = Player(250, 250, pygame.Color("#2200FE"))
board = Board(10, 10, pygame.Color("#777777"))
cow = Cow(200, 350, 20, 20, pygame.Color("#FFFFFF"))
box = Box(200, 550, 50, 50, pygame.Color("#783E00"))
walls = [
    Wall(400, 50, 40, 500, pygame.Color("#474747")),
    Wall(400, 700, 500, 40, pygame.Color("#474747")),
]

speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")


    keys = pygame.key.get_pressed()

    player.move(keys, walls, box, board)
    cow.update(walls, board)


    screen.blit(board.image, (board.x, board.y))
    screen.blit(cow.image, cow.rect)
    screen.blit(player.image, player.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    screen.blit(box.image, box.rect)

    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()

#helloworl