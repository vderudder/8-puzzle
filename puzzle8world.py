from environments import SimulatedEnvironment

def update_zero(brd):
    if 0 in brd[0]:
        return [0, brd[0].index(0)]  # el primer valor es el nivel, el segundo es la posicion del 0 en el vector
    elif 0 in brd[1]:
        return [1, brd[1].index(0)]
    elif 0 in brd[2]:
        return [2, brd[2].index(0)]
    else:
        raise Exception("El tablero no es valido")


class PuzzleEnvironment(SimulatedEnvironment):

    def __init__(self, board, width: int):
        super(PuzzleEnvironment, self).__init__()
        self._zero_at = update_zero(board)
        self._board = board
        self._width = width
        self._agents_locations = {}  # maps agent id with its location

    def add(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).add(agent_id)
        self._agents_locations[agent_id] = 0

    def remove(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).remove(agent_id)
        self._agents_locations.pop(agent_id, None)

    def get_property(self, agent_id: int, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id, "board": self._board}
            return response
        else:
            return {}

    def _move_left(self):
        brd = self._board
        at = self._zero_at

        a, b = min(at[1], at[1] - 1), max(at[1], at[1] - 1)  # a y b son indices (posicion)

        if a < 0 or b < 0:
            print("No se puede hacer este movimiento")
        else:
            brd[at[0]][a], brd[at[0]][b] = brd[at[0]][b], brd[at[0]][
                a]  # se intercambia la posicion dentro del nivel indicado
            self._zero_at = update_zero(brd)

    def _move_right(self):
        brd = self._board
        at = self._zero_at

        a, b = min(at[1], at[1] + 1), max(at[1], at[1] + 1)  # a y b son indices (posicion)

        if a > 2 or b > 2:
            print("No se puede hacer este movimiento")
        else:
            brd[at[0]][a], brd[at[0]][b] = brd[at[0]][b], brd[at[0]][
                a]  # se intercambia la posicion dentro del nivel indicado
            self._zero_at = update_zero(brd)

    def _move_up(self):
        brd = self._board
        at = self._zero_at

        a, b = min(at[0], at[0] - 1), max(at[0], at[0] - 1)

        if a < 0 or b < 0:
            print("No se puede hacer este movimiento")
        else:
            brd[a][at[1]], brd[b][at[1]] = brd[b][at[1]], brd[a][
                at[1]]  # se intercambia el nivel pero se mantiene la posicion dentro
            self._zero_at = update_zero(brd)

    def _move_down(self):
        brd = self._board
        at = self._zero_at

        a, b = min(at[0], at[0] + 1), max(at[0], at[0] + 1)

        if a > 2 or b > 2:
            print("No se puede hacer este movimiento")
        else:
            brd[a][at[1]], brd[b][at[1]] = brd[b][at[1]], brd[a][
                at[1]]  # se intercambia el nivel pero se mantiene la posicion dentro
            self._zero_at = update_zero(brd)

    def take_action(self, agent_id: int, action_name: str, params: dict = {}) -> None:
        if agent_id in self._agents:
            if action_name == "move":
                if "direction" in params and params["direction"] == "left":
                    self._move_left()
                elif "direction" in params and params["direction"] == "right":
                    self._move_right()
                elif "direction" in params and params["direction"] == "up":
                    self._move_up()
                elif "direction" in params and params["direction"] == "down":
                    self._move_down()
