import random
import numpy as np

from environments import SimulatedEnvironment


class PuzzleEnvironment(SimulatedEnvironment):
    def __new__(cls):
        return super().__new__(cls)

    def __init__(self):
        super(PuzzleEnvironment, self).__init__()
        self._matrix = np.random.randint(10, size=(3, 3))  # esto crearia una matriz de 3x3 con numeros del 0 al 9 en lugares random siendo 0 la ficha vacia
        self._agents_locations = {}                     # maps agent id with its location

    def add(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).add(agent_id)
        self._agents_locations[agent_id] = 0

    def remove(self, agent_id: int) -> None:
        super(PuzzleEnvironment, self).remove(agent_id)
        self._agents_locations.pop(agent_id, None)

    def _show_board(self):
        response = {"board": self._matrix}
        return response

    def get_property(self, agent_id: int, property_name: str) -> dict:
        if agent_id in self._agents:
            response = {"agent": agent_id, "board": self._show_board}
            return response
        else:
            return {}

    def _move_agent_left(self, agent_id: int):
        self._agents_locations[agent_id] = max(self._agents_locations[agent_id] - 1, 0)

    def _move_agent_right(self, agent_id: int):
        self._agents_locations[agent_id] = min(self._agents_locations[agent_id] + 1, self._length - 1)

    def _move_agent_up(self, agent_id: int):
        self._agents_locations[agent_id] = min(self._agents_locations[agent_id] + 1, self._length - 1) #modificar

    def _move_agent_down(self, agent_id: int):
        self._agents_locations[agent_id] = min(self._agents_locations[agent_id] + 1, self._length - 1) #modificar


   def take_action(self, agent_id: int, action_name: str, params: dict = {}) -> None:
        if agent_id in self._agents:
            if action_name == "move":
                if "direction" in params and params["direction"] == "left":
                    self._move_agent_left(agent_id)
                elif "direction" in params and params["direction"] == "right":
                    self._move_agent_right(agent_id)
                elif "direction" in params and params["direction"] == "up":
                    self._move_agent_up(agent_id)
                elif "direction" in params and params["direction"] == "down":
                    self._move_agent_down(agent_id)
