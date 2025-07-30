import random

class WumpusWorld:
    def __init__(self, size):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.place_elements()

    def place_elements(self):
        self.grid[0][0] = 'Start'
        self.place('Wumpus')
        self.place('Gold')
        for _ in range(3): self.place('Pit')

    def place(self, thing):
        while True:
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            if self.grid[x][y] == '':
                self.grid[x][y] = thing
                break
