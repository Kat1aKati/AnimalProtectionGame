import pygame

pygame.init()
screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
pygame.display.set_caption("game")

clock = pygame.time.Clock()

class Board(pygame.sprite.Sprite):
    def init(self, x, y, color=(0, 0, 255)):
        super().init()
        self.image = pygame.Surface((1480, 780))
        self.image.fill(color)
        self.color = color
        self.x = x
        self.y = y




class Player():
    def init(self, x, y, color):
        super().init()
        self.image = pygame.Surface((25, 25))
        self.image.fill(color)
        self.color = color
        self.x = x
        self.y = y

class Enviroment():
    print("test")




player = Player()
board = Board()

c = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5



    screen.blit(board.image, (board.x, board.y))
    screen.blit(player.image, (player.x, player.y))

    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()