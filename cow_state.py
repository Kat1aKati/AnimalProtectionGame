class CowState:
    def __init__(self, hero):
        self.hero = hero
        self.name = self.__class__.__name__

    def enter(self): pass
    def exit(self): pass
    def update(self, keys): pass

class Idle(CowState):
    def enter(self):
        self.hero.velocity_y = 5

    def update(self, keys):
        self.hero.rect.y += self.hero.velocity_y
        if self.hero.rect.bottom >= 500:
            self.hero.rect.bottom = 500
            self.hero.change_state(Scared(self.hero))

class Scared(CowState):
    def enter(self):
        self.hero.velocity_y = 5

    def update(self, keys):
        self.hero.rect.y += self.hero.velocity_y
        if self.hero.rect.bottom >= 500:
            self.hero.rect.bottom = 500
            self.hero.change_state(Idle(self.hero))