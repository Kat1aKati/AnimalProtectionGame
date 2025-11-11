import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
pygame.display.set_caption("game")

clock = pygame.time.Clock()

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, color=(0, 0, 255)):
        super().__init__()
        self.image = pygame.Surface((1480, 780))
        self.image.fill(color)
        self.color = color
        self.x = x
        self.y = y

#onoToŽije

class Player():
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = color
        self.x = x
        self.y = y

#class Enviroment():

class Wall():
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 500))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
        self.color = color
        self.x = x
        self.y = y


player = Player(250, 250, (0, 0, 255))
board = Board(10, 10, (50, 50, 50))
wall = Wall(400, 50, (150, 150, 150))

speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")

    keys = pygame.key.get_pressed()
   
    if keys[pygame.K_LEFT]:
        player.rect.x -= speed
        if player.rect.colliderect(wall.rect):
            player.rect.left = wall.rect.right
    if keys[pygame.K_RIGHT]:
        player.rect.x += speed
        if player.rect.colliderect(wall.rect):
            player.rect.right = wall.rect.left
    if keys[pygame.K_UP]:
        player.rect.y -= speed
        if player.rect.colliderect(wall.rect):
            player.rect.top = wall.rect.bottom
    if keys[pygame.K_DOWN]:
        player.rect.y += speed
        if player.rect.colliderect(wall.rect):
            player.rect.bottom = wall.rect.top


#ono to proste ide

    screen.blit(board.image, (board.x, board.y))
    screen.blit(player.image, player.rect)
    screen.blit(wall.image, wall.rect)


    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()