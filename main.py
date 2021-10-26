from puzzle8world import PuzzleEnvironment
from puzzle8agent import PuzzleAgent, MoveDirection


if __name__ == '__main__':
    board = 1,2,3, 4,0,6, 7,5,8
    env = PuzzleEnvironment(board, 3)

    agent = PuzzleAgent(env)
    print(agent.id)

    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.UP)
    agent.print_state()

