from environments import SimulatedSensor, SimulatedActuator, SimulatedEnvironment
from agents import Agent


class BoardSensor(SimulatedSensor):

    def sense(self):
        response = self._env.get_property(self._agent.id, property_name="board")
        return response["board"]


from enum import Enum, unique


@unique
class MoveDirection(Enum):
    LEFT = (0, -1)  # ver
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


class MoverActuator(SimulatedActuator):

    def act(self, direction: MoveDirection = MoveDirection.RIGHT):
        if direction == MoveDirection.RIGHT:
            d = "right"
        elif direction == MoveDirection.LEFT:
            d = "left"
        elif direction == MoveDirection.UP:
            d = "up"
        else:
            d = "down"

        request_info = {"direction": d}
        self._env.take_action(self._agent.id, "move", request_info)


class PuzzleAgent(Agent):

    def function(self, percept):
        pass

    def __init__(self, env: SimulatedEnvironment):
        super().__init__()
        env.add(self.id)

        mover = MoverActuator(env)
        mover.agent = self
        self.add_actuator("mover", mover)

        board = BoardSensor(env)
        board.agent = self
        self.add_sensor("board", board)

        # self.setup_function()

    def print_state(self):
        print("Este es el tablero:")
        print(self._sensors["board"].sense())
