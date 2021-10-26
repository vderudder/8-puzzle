from environments import SimulatedEnvironment


class PuzzleEnvironment(SimulatedEnvironment):

    def __init__(self, board, width: int, zero_at):
        super(PuzzleEnvironment, self).__init__()
        if zero_at is None:
            if 0 in board[0]:
                self._zero_at = [0, board[0].index(0)]
            elif 0 in board[1]:
                self._zero_at = [1, board[1].index(0)]
            elif 0 in board[2]:
                self._zero_at = [2, board[2].index(0)]
        self._board = board
        self._width = width
        self._agents_locations = {}  # maps agent id with its location

    def add(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).add(agent_id)
        self._agents_locations[agent_id] = 0

    def remove(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).remove(agent_id)
        self._agents_locations.pop(agent_id, None)

    """def _show_board(self):
        response = {"board": self._board}
        return response
        """

    def get_property(self, agent_id: int, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id, "board": self._board}
            return response
        else:
            return {}

    def _move_left(self):
        at = self._zero_at
        brd = self._board

        a, b = min(at[1], at[1] - 1), max(at[1], at[1] - 1)  # a y b son indices (posicion)

        brd[at[0]][a], brd[at[0]][b] = brd[at[0]][b], brd[at[0]][a]

        update (zeroat)     # en cada metodo

    def _move_right(self):
        at = self._zero_at
        brd = self._board

        a, b = min(at[1], at[1] + 1), max(at[1], at[1] + 1)  # a y b son indices (posicion)

        brd[at[0]][a], brd[at[0]][b] = brd[at[0]][b], brd[at[0]][a]

    def _move_up(self):
        at = self._zero_at
        brd = self._board

        a, b = min(at, at - self._width), max(at, at - self._width)

        brd[a], brd[b] = brd[b], brd[a]

    def _move_down(self):
        at = self.zero_at
        brd = self._board

        a, b = min(at, at + self._width), max(at, at + self._width)

        brd[a], brd[b] = brd[b], brd[a]

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
