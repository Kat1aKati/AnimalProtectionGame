import pygame
import world

class Player:
    def __init__(self, x, y, color, game):
        super().__init__()
        self.image = pygame.Surface((75, 75))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.x = x
        self.y = y
        self.speed = 5

    def move(self, keys, board):
        dx, dy = 0, 0
        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed
        if keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_s]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed
        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed

        self.rect.x += dx
        self.handle_collisions(dx, 0)
        self.rect.y += dy
        self.handle_collisions(0, dy)

        board.keep_inside(self.rect)

    def handle_collisions(self, dx, dy):
        for wall in world.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom

        # block against wheat unless it's already picked up
        wheat_obj = world.wheat
        if wheat_obj is not None and not wheat_obj.picked_up and self.rect.colliderect(wheat_obj.rect):
            if dx > 0:
                self.rect.right = wheat_obj.rect.left
            if dx < 0:
                self.rect.left = wheat_obj.rect.right
            if dy > 0:
                self.rect.bottom = wheat_obj.rect.top
            if dy < 0:
                self.rect.top = wheat_obj.rect.bottom

        for box in world.boxes:
            if self.rect.colliderect(box.rect):
                if box.push(dx, dy, world.walls):
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
