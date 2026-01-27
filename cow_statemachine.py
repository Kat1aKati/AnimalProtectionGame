from object import Wheat

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
        pass
        


class Scared(CowState):
    def enter(self):
        print("entered scared state")

    def update(self):
        pass