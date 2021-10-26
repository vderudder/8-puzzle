from puzzle8world import PuzzleEnvironment
from puzzle8agent import PuzzleAgent, MoveDirection


if __name__ == '__main__':
    board = [[1, 2, 5], [4, 0, 6], [7, 3, 8]]
    env = PuzzleEnvironment(board, 3, None)
    print("Paso el constructor")

    agent = PuzzleAgent(env)
    print("id del agente: {}".format(agent.id))

    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
    agent.print_state()
    agent.actuators["mover"].act(direction=MoveDirection.LEFT)
    agent.print_state()

