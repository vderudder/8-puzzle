from puzzle8world import PuzzleEnvironment
from puzzle8agent import PuzzleAgent, MoveDirection


if __name__ == '__main__':
    env = PuzzleEnvironment(2, True)

    agent = PuzzleAgent(env)
    print(agent.id)

    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.LEFT)
    agent.print_state()

