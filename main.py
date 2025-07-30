from agent import Agent
from world import WumpusWorld

if __name__ == "__main__":
    world = WumpusWorld(4)  # 4x4 grid
    agent = Agent(world)
    agent.play()
