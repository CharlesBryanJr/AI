'''
create robot vacuum that cleans all the floors of a grid.
main creates an instance of RoboVac (your code) and provides:
- grid size
- loc of robovac
- list of x,y,w,h tuples are instance of rectangular blocks

goal: visit all tiles
exec will : create instance and in game loop call : nextMove()  ??
'''

import random
import numpy as np


class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x, y, width, height)
        self.visited = set()  # Keep track of visited cells

        # fill in with your info
        self.name = "Charles Bryan"
        self.id = "49350684"

        # create a set of all blocked tiles
        self.block_tiles_set = set()
        for block in self.block_list:
            for x in range(block[0], block[0] + block[2]):
                for y in range(block[1], block[1] + block[3]):
                    self.block_tiles_set.add((x, y))

    def get_next_move(self, current_pos):
        self.pos = current_pos # Update the current position

        move_direction = self.get_valid_neighbor_direction()
        if move_direction is None:
            move_direction = random.choice([0, 1, 2, 3])

        return move_direction


    def get_valid_neighbor_direction(self):
        self.visited.add(self.pos)

        # Define potential moves
        moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Up, Right, Down, Left
        directions = [0, 1, 2, 3]  # Corresponding direction indices

        # Check for unvisited and valid adjacent cells
        for move, direction in zip(moves, directions):
            next_pos = (self.pos[0] + move[0], self.pos[1] + move[1])

            is_next_pos_x_valid = 0 <= next_pos[0] < self.room_width
            is_next_pos_y_valid = 0 <= next_pos[1] < self.room_height
            is_next_pos_not_visited = next_pos not in self.visited
            is_next_pos_not_a_block = next_pos not in self.block_tiles_set
            is_next_pos_valid = is_next_pos_x_valid and is_next_pos_y_valid and is_next_pos_not_visited and is_next_pos_not_a_block
            if is_next_pos_valid:
                return direction

        # None of the neighbor are valid
        return None



