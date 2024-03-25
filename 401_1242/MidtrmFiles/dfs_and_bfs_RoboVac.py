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
from collections import deque



class RoboVac:
    def __init__(self, config_list):
        self.room_width, self.room_height = config_list[0]
        self.pos = config_list[1]  # starting position of vacuum
        self.block_list = config_list[2]  # blocks list (x, y, width, height)

        # fill in with your info
        self.name = "Charles Bryan"
        self.id = "49350684"


        self.start = True
        self.start_node = config_list[1]

        self.came_from = {}
        self.backtrack_moves = []
        self.last_pos = None

        self.random_dir = {1, 2, 3, 4}

        # Initialize block_tiles_set based on the block_list
        self.block_tiles_set = set()
        for block in self.block_list:
            for x in range(block[0], block[0] + block[2]):
                for y in range(block[1], block[1] + block[3]):
                    self.block_tiles_set.add((x, y))

        # Initialize free_tiles_set
        self.uncleaned_tiles = set((x, y) for x in range(self.room_width) for y in range(self.room_height))
        self.uncleaned_tiles -= self.block_tiles_set

        # Initialize variables for DFS
        self.max_depth = self.room_width * self.room_height
        self.dfs_stack = [(self.pos, [self.pos])]
        self.visited = set()

        # Initialize variables for BFS
        self.bfs_queue = deque([(self.pos, [self.pos])])

        # find clean title variables
        self.next_clean_tile = None
        self.moving_toward_clean_title = False
        self.x_iteration_towards_tile = 0
        self.x_iterations_towards_tile = 0
        self.y_iteration_towards_tile = 0
        self.y_iterations_towards_tile = 0
        self.total_iterations_towards_tile = abs(self.x_iterations_towards_tile) + abs(self.y_iterations_towards_tile)


    def get_next_move(self, current_pos):
        self.pos = current_pos  # Update the current position

        back_tracked_to_start = self.pos == self.start_node and not self.start
        if back_tracked_to_start:
            print('back_tracked_to_start')
            print('back_tracked_to_start')
            print('back_tracked_to_start')
            self.reset_all_variables()
            move_direction = self.bfs_iter() # from start node, run BFS
            if move_direction is not None:
                self.last_pos = self.pos
                return move_direction
        self.start = False

        print('')
        print('get_next_move')

        if self.pos == self.last_pos:
            print('STUCK')
            print('STUCK')
            print('STUCK')

        move_direction = self.dfs_iter(self.max_depth)  # from current position, run depth-limited DFS
        if move_direction is not None:
            self.last_pos = self.pos
            return move_direction
        else:
            # Backtrack to start once DFS is finished
            if self.backtrack_moves:
                print('!!! Backtracking from dead-end !!!')
                self.last_pos = self.pos
                # Use the last stored backtrack move
                backtrack_move = self.backtrack_moves.pop()
                return backtrack_move


    def dfs_iter(self, limit):
        while self.dfs_stack:
            (vertex, path) = self.dfs_stack.pop()

            if len(path) > limit:
                continue  # Ignore paths longer than limit

            if vertex not in self.visited:
                self.visited.add(vertex)
                self.uncleaned_tiles.discard(vertex)

                directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                for i, (dx, dy) in enumerate(directions):
                    move_direction = i
                    opposite_move_direction = self.get_opposite_direction(move_direction)
                    self.next_pos = (vertex[0] + dx, vertex[1] + dy)
                    if self.is_next_pos_valid(self.next_pos, self.room_width, self.room_height):
                        self.dfs_stack.append((self.next_pos, path + [self.next_pos]))
                        self.came_from[self.next_pos] = vertex
                        self.backtrack_moves.append(opposite_move_direction)
                        return move_direction

        return None


    def bfs_iter(self):
        print('')
        print('bfs_iter')
        print('self.bfs_queue', self.bfs_queue)

        while self.bfs_queue:
            vertex, path = self.bfs_queue.popleft()
            if vertex not in self.visited or vertex == self.start_node:
                print('valid bfs vertex', vertex)

                self.visited.add(vertex)
                self.uncleaned_tiles.discard(vertex)

                # Process the vertex and return the direction if a move is made
                # Otherwise, enqueue the adjacent vertices
                for move_direction, (dx, dy) in enumerate([(0, -1), (1, 0), (0, 1), (-1, 0)]):
                    next_pos = (vertex[0] + dx, vertex[1] + dy)
                    if self.is_next_pos_valid(next_pos, self.room_width, self.room_height):
                        print('is_next_pos_valid - True -', next_pos)
                        self.bfs_queue.append((next_pos, path + [next_pos]))
                        print('self.bfs_queue', self.bfs_queue)
                        self.came_from[next_pos] = vertex
                        print('move_direction ', move_direction)
                        return move_direction
                    else:
                        print('is_next_pos_valid - False -', next_pos)

        print('bfs_iter returned NONE')
        return None  # No more moves available


    def is_next_pos_valid(self, next_pos, room_width, room_height):
        x, y = next_pos
        is_next_pos_x_valid = 0 <= x < self.room_width
        is_next_pos_y_valid = 0 <= y < self.room_height
        return (is_next_pos_x_valid and is_next_pos_y_valid and next_pos not in self.block_tiles_set and next_pos not in self.visited)


    def calculate_direction(self, next_pos):
        # Calculate the direction based on the current position and the next position
        dx = next_pos[0] - self.pos[0]
        dy = next_pos[1] - self.pos[1]
        if dx == 1:
            return 1  # right
        elif dx == -1:
            return 3  # left
        elif dy == 1:
            return 2  # down
        elif dy == -1:
            return 0  # up
        return None


    def get_opposite_direction(self, direction):
        opposite_directions = {1: 3, 3: 1, 2: 0, 0: 2}
        return opposite_directions.get(direction, None)


    def reset_all_variables(self):
        print('reset_all_variables')
        self.start = True
        self.start_node = self.pos
        self.last_pos = None

        self.came_from = {}
        self.backtrack_moves = []

        self.random_dir = {1, 2, 3, 4}

        # Initialize variables for DFS
        self.max_depth = self.room_width * self.room_height
        self.dfs_stack = [(self.pos, [self.pos])]
        self.visited = set()

