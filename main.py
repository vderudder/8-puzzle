from puzzle8world import PuzzleEnvironment
from puzzle8agent import PuzzleAgent, MoveDirection
import ast


if __name__ == '__main__':
    # board = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

    board = input("Ingrese el tablero: ")
    arr = []
    arr.append(ast.literal_eval('[%s]' % board))
    board = arr[0]

    env = PuzzleEnvironment(board, 3)

    agent = PuzzleAgent(env)

    agent.print_state()

    var = True
    while var:
        inp = input("Exit? (y exits)")
        if inp == "y":
            break
        else:
            print("Para mover la ficha: use 'i' para izq, 'd' para der, 'ab' para abajo, 'ar' para arriba")
            mov = input("Movimiento: ")
            if mov == "i":
                agent.actuators["mover"].act(direction=MoveDirection.LEFT)
                agent.print_state()
            elif mov == "d":
                agent.actuators["mover"].act(direction=MoveDirection.RIGHT)
                agent.print_state()
            elif mov == "ab":
                agent.actuators["mover"].act(direction=MoveDirection.DOWN)
                agent.print_state()
            elif mov == "ar":
                agent.actuators["mover"].act(direction=MoveDirection.UP)
                agent.print_state()

