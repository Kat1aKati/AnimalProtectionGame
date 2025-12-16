#taže, prvy level by sme mohli dať ako tutorial. Hybal by si sa WASD (treba pridať) alebo šipky
#V prvom leveli by mohol player odtlačiť ten pushable box na nejake miesto aby sa mu otvorili dvere a pustili by ho do dalšieho levelu
#NPC (to ai) by mohlo mať nejaky hitbox aby sa s nim mohlo hybať, možno interagovať
#commit needed!


#tell me to record voice lines as a "main" charachter for the game with ready lines to go

import pygame
import random
import time
from statemachine import StateMachine


pygame.init()
screen = pygame.display.set_mode((1500, 800), pygame.RESIZABLE)
pygame.display.set_caption("game")
clock = pygame.time.Clock()

class Board(pygame.sprite.Sprite):
    def __init__(self, x, y, color=None):
        super().__init__()
        self.image = pygame.image.load("image/floor.png").convert_alpha() #pozadie
        self.rect = self.image.get_rect(topleft = (x, y))
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
        self.image = pygame.Surface((75, 75)) #player (change)
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))
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
        self.handle_collisions( dx, 0)
        self.rect.y += dy
        self.handle_collisions( 0, dy)

        board.keep_inside(self.rect)

    def handle_collisions(self, dx, dy):

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

        for box in boxes:

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
        self.image = pygame.image.load("image/cow.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (sx, sy))
        self.rect = self.image.get_rect(topleft=(x, y))
        
        self.speed = 2
        self.change_direction_time = 0
        self.dx, self.dy = 0, 0 

        self.state_machine = StateMachine(self)
        


    def update(self, walls, board):
        
        if not self.state_machine.current_state:
            self.change_state(Idle(self))
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

        

    def change_state(self, state):
        self.state_machine.change_state(state)


class CowState:
    def __init__(self, hero):
        self.hero = hero
        self.name = self.__class__.__name__

    def enter(self): pass
    def exit(self): pass
    def update(self, keys): pass

class Idle(CowState):
    def enter(self):
        print("entered idle state")

    def update(self):
        if wheat.picked_up == True:
            self.hero.change_state(Scared(self.hero))
        


class Scared(CowState):
    def enter(self):
        print("entered scared state")

    def update(self):
        pass



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

    def placebox(self):
        if self.rect.collidelist(tiles):
            return True
        else:
            False

class Tile(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)
        self.activated = False
        self.was_activated = False
    
    def activate_tile(self):
        if self.activated == False:
            self.activated = True
        else:
            self.activated = False
        
        print("Tile activated:" , self.activated)

class Door(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)
        self.opened = False
   
    def shift_doors(self):
        self.opened = all(tile.activated for tile in tiles)
        

                
#3 states - idle, scared, wheat

class Wheat(Object):
    def __init__(self, x, y, sx, sy, color):
        super().__init__(x, y, sx, sy, color)
        self.picked_up = False


boxes = []
tiles = []

player = Player(250, 250, pygame.Color("#2200FE"))
board = Board(10, 10, pygame.Color("#777777"))
cow = Cow(200, 350, 49, 40, pygame.Color("#FFFFFF"))
box1 = Box(200, 550, 50, 50, pygame.Color("#783E00"))
box2 = Box(500, 200, 50, 50, pygame.Color("#783E00"))

walls = [
    Wall(400, 50, 40, 400, pygame.Color("#474747")),
    Wall(400, 700, 1080, 40, pygame.Color("#474747")),
    Wall(1100, 250, 40, 450, pygame.Color("#474747"))
]
tile1 = Tile(500, 500, 75, 75, pygame.Color("#00FF00"))
door = Door(300, 350, 100, 50, pygame.Color("#FF0095"))
wheat = Wheat(150, 100, 10, 10, pygame.Color("#D3BE00"))


boxes.append(box1)
boxes.append(box2)

tiles.append(tile1)
#x, y, size x, sixe y

speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")

    keys = pygame.key.get_pressed()

    player.move(keys, board)
    cow.update(walls, board)

    if player.rect.colliderect(wheat.rect):
        wheat.picked_up = True
        cow.state = wheat
    
    for tile in tiles:
        collision_result = tile.rect.collidelist(boxes)
        colliding_now = collision_result != -1

        # ENTERED
        if colliding_now and not tile.was_activated:
            tile.activate_tile()

        # EXITED
        if not colliding_now and tile.was_activated:
            tile.activate_tile()

        tile.was_activated = colliding_now

    print(tile.activated)
    if door.opened == True:

        print("door opened")


    cow.state_machine.update()

    screen.blit(board.image, (board.x, board.y))
    screen.blit(cow.image, cow.rect)
    screen.blit(door.image, door.rect)
    for tile in tiles:
        screen.blit(tile.image, tile.rect)
        
    screen.blit(player.image, player.rect)
    
    for wall in walls:
        screen.blit(wall.image, wall.rect)

    for box in boxes:
        screen.blit(box.image, box.rect)
    
    screen.blit(wheat.image, wheat.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

