class Agent:
    def __init__(self, world):
        self.world = world
        self.position = (0, 0)
        self.knowledge = {}
        self.visited = set()

    def play(self):
        while True:
            x, y = self.position
            cell = self.world.grid[x][y]
            print(f"At {x},{y} -> {cell}")
            self.visited.add((x, y))
            if cell == 'Wumpus' or cell == 'Pit':
                print("Game Over!")
                break
            if cell == 'Gold':
                print("Gold found! You win!")
                break
            self.move()

    def move(self):
        x, y = self.position
        # Try to move to an adjacent unvisited cell
        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.world.size and 0 <= ny < self.world.size and (nx, ny) not in self.visited:
                self.position = (nx, ny)
                return
