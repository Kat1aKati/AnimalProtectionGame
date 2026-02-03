import pygame



wheat = None

class Object:
    def __init__(self, x, y, sx, sy, color, game):
        self.image = pygame.Surface((sx, sy))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.color = color
        self.x = x
        self.y = y
        self.game = game

class Wall(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color, game)

class Box(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color, game)

    def push(self, dx, dy, walls, visited=None):

        if visited is None:
            visited = set()
        if id(self) in visited:
            return False
        visited.add(id(self))

        orig = self.rect.copy()

        if dx:
            self.rect.x += dx
            for wall in self.game.walls:
                if self.rect.colliderect(wall.rect):
                    self.rect = orig
                    return False
            for other in self.game.boxes:
                if other is self:
                    continue
                if self.rect.colliderect(other.rect):

                    if not other.push(dx, 0, walls, visited):
                        self.rect = orig
                        return False


        if dy:
            self.rect.y += dy
            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    self.rect = orig
                    return False
            for other in self.game.boxes:
                if other is self:
                    continue
                if self.rect.colliderect(other.rect):

                    if not other.push(0, dy, walls, visited):
                        self.rect = orig
                        return False

        self.game.board.keep_inside(self.rect)
        return True

    def placebox(self):
        if self.rect.collidelist(self.game.tiles):
            return True
        else:
            False

class Tile(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color, game)
        self.activated = False
        self.was_activated = False
    
    def activate_tile(self):
        if self.activated == False:
            self.activated = True
        else:
            self.activated = False
        
        print("Tile activated:" , self.activated)

class Door(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color, game)
        self.opened = False
   
    def shift_doors(self):
        self.opened = all(tile.activated for tile in self.game.tiles)
        
def crash(box, dx, dy):
    return box.push(dx, dy, walls)
                


#3 states - idle, scared, wheat

class Wheat(Object):
    def __init__(self, x, y, sx, sy, color, game):
        super().__init__(x, y, sx, sy, color, game)
        self.picked_up = False