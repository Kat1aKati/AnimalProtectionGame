import pygame

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
            self.current_state.update()

    def get_state_name(self):
        return self.current_state.name if self.current_state else "None"
