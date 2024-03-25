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

        self.last_pos = None

        # fill in with your info
        self.name = "Charles Bryan"
        self.id = "49350684"

        # Initialize block_tiles_set based on the block_list
        self.block_tiles_set = set()
        for block in self.block_list:
            for x in range(block[0], block[0] + block[2]):
                for y in range(block[1], block[1] + block[3]):
                    self.block_tiles_set.add((x, y))

        # Initialize variables for DFS
        self.max_depth = self.room_width * self.room_height
        self.dfs_stack = [(self.pos, [self.pos])]
        self.visited = set()


    def get_next_move(self, current_pos):
        self.pos = current_pos # Update the current position

        move_direction = self.dfs_iter(self.max_depth)
        if move_direction is not None:
            self.last_pos = self.pos
            return move_direction
        else:
            move_direction = random.choice([0, 1, 2, 3])

        # since DFS returned NONE, we want to restart it on restart DFS on next tile
        self.last_pos = self.pos
        new_pos = self.get_new_pos(move_direction, self.pos)
        self.dfs_stack = [(new_pos, [new_pos])]

        return move_direction


    def dfs_iter(self, limit):
        while self.dfs_stack:
            (vertex, path) = self.dfs_stack.pop()

            if len(path) > limit:
                continue  # Ignore paths longer than limit

            if vertex not in self.visited:
                self.visited.add(vertex)

                directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                for i, (dx, dy) in enumerate(directions):
                    move_direction = i
                    self.next_pos = (vertex[0] + dx, vertex[1] + dy)

                    is_next_pos_x_valid = 0 <= self.next_pos[0] < self.room_width
                    is_next_pos_y_valid = 0 <= self.next_pos[1] < self.room_height

                    is_next_pos_valid = is_next_pos_x_valid and is_next_pos_y_valid and self.next_pos not in self.block_tiles_set and self.next_pos not in self.visited
                    if is_next_pos_valid:
                        self.dfs_stack.append((self.next_pos, path + [self.next_pos]))
                        return move_direction

        return None


    def get_new_pos(self, dir, curr_pos):
        x, y = curr_pos
        if dir == 0:  # Up
            return (x, y - 1)
        elif dir == 1:  # Right
            return (x + 1, y)
        elif dir == 2:  # Down
            return (x, y + 1)
        elif dir == 3:  # Left
            return (x - 1, y)
        else:
            return 'Invalid direction'



