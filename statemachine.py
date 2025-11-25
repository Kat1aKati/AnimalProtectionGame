import pygame


class State:
    def __init__(self, hero):
        self.hero = hero
        self.name = self.__class__.__name__

    def enter(self): pass
    def exit(self): pass
    def update(self, keys): pass


class FallingState(State):
    def enter(self):
        self.hero.velocity_y = 5

    def update(self, keys):
        self.hero.rect.y += self.hero.velocity_y
        if self.hero.rect.bottom >= 500:
            self.hero.rect.bottom = 500
            self.hero.change_state(GroundedState(self.hero))
    

class GroundedState(State):
    def enter(self):
        self.hero.velocity_y = 0

    def update(self, keys):
        if keys[pygame.K_SPACE]:
            self.hero.change_state(JumpingState(self.hero))
            

        if keys[pygame.K_a]:
            self.hero.velocity_x = -6
        elif keys[pygame.K_d]:
            self.hero.velocity_x = 6
        else:
            self.hero.velocity_x = 0



class JumpingState(State):
    def enter(self):
        self.hero.velocity_y = -30  

    def update(self, keys):
        self.hero.velocity_y += 0.5  

        if self.hero.velocity_y > 0:
            self.hero.change_state(FallingState(self.hero))




# --- STATE MACHINE WRAPPER ---
class StateMachine:
    def __init__(self, hero):
        self.hero = hero
        self.current_state = None

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.exit()
        self.current_state = new_state
        self.current_state.enter()

    def update(self, keys):
        if self.current_state:
            self.current_state.update(keys)

    def get_state_name(self):
        return self.current_state.name if self.current_state else "None"


# --- HERO CLASS ---
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity_y = 0
        self.velocity_x = 0

        self.state_machine = StateMachine(self)
        self.change_state(FallingState(self))  # starts falling

    def change_state(self, state):
        self.state_machine.change_state(state)

    def update(self, keys):
        # Let state handle logic & input
        self.state_machine.update(keys)

        # Then apply physics consistently
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # Basic gravity
        if self.rect.bottom < 500:
            self.velocity_y += 1
        else:
            self.rect.bottom = 500
            self.velocity_y = 0


    def get_state_name(self):
        return self.state_machine.get_state_name()