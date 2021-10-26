from environments import SimulatedEnvironment


class PuzzleEnvironment(SimulatedEnvironment):
    def __new__(cls, board, width, zero_at=None):
        if zero_at is None:
            zero_at = board.index(0)

        return super().__new__(cls, board, width, zero_at)

    def __init__(self, board, width, zero_at):
        super(PuzzleEnvironment, self).__init__()
        self._board = list(board)  # randomizar el tablero
        self._width = width
        self._zero_at = zero_at
        self._agents_locations = {}  # maps agent id with its location

    def add(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).add(agent_id)
        self._agents_locations[agent_id] = 0

    def remove(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).remove(agent_id)
        self._agents_locations.pop(agent_id, None)

    def _show_board(self):
        response = {"board": self._board}
        return response

    def get_property(self, agent_id: int, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id, "board": self._show_board}
            return response
        else:
            return {}

    def _move_left(self):
        at = self._zero_at
        brd = self._board

        a, b = min(at, at - 1), max(at, at - 1)

        brd[a], brd[b] = brd[b], brd[a]

    def _move_right(self):
        at = self._zero_at
        brd = self._board

        a, b = min(at, at - 1), max(at, at + 1)

        brd[a], brd[b] = brd[b], brd[a]

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
                self._move_left(agent_id)
            elif "direction" in params and params["direction"] == "right":
                self._move_right(agent_id)
            elif "direction" in params and params["direction"] == "up":
                self._move_up(agent_id)
            elif "direction" in params and params["direction"] == "down":
                self._move_down(agent_id)
