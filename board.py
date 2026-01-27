import pygame

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, color=None):
        super().__init__()
        self.image = pygame.image.load("AnimalProtectionGame/image/floor.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
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
