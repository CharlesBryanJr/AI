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

        # fill in with your info
        self.name = "Charles Bryan"
        self.id = "49350684"

        self.came_from = {}
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

        # find clean title variables
        self.next_clean_tile = None
        self.moving_toward_clean_title = False
        self.x_iteration_towards_tile = 0
        self.x_iterations_towards_tile = 0
        self.y_iteration_towards_tile = 0
        self.y_iterations_towards_tile = 0
        self.total_iterations_towards_tile = abs(self.x_iterations_towards_tile) + abs(self.y_iterations_towards_tile)


    def get_next_move(self, current_pos):
        self.pos = current_pos # Update the current position
        print('')
        print('self.uncleaned_tiles count ', len(self.uncleaned_tiles))
        print('get_next_move')
        print('self.last_pos ', self.last_pos)
        print('self.pos ', self.pos)


        if self.pos == self.last_pos:
            print('STUCK')
            print('STUCK')
            print('STUCK')

            move_direction = self.random_dir.pop()
            print('random_dir', self.random_dir)
            print('move_direction ', move_direction)

            self.reset_moving_toward_clean_tile_variables()
            self.last_pos = self.pos
            # return move_direction
        else:
            self.reset_random_dir()

        if self.moving_toward_clean_title:
            self.visited.add(self.pos)
            return self.move_torward_clean_title()

        move_direction = self.dfs_iter(self.max_depth) # from current position, run depth-limited DFS search
        if move_direction is not None:
            self.last_pos = self.pos
            return move_direction
        else:
            return None


    def dfs_iter(self, limit):
        print('')
        print('dfs_path')
        print('self.dfs_stack ', self.dfs_stack)
        while self.dfs_stack:
            (vertex, path) = self.dfs_stack.pop()

            if len(path) > limit:
                continue  # Ignore paths longer than limit

            print('vertex ', vertex)
            print('vertex in self.visited', vertex in self.visited)
            if vertex not in self.visited:
                self.visited.add(vertex)
                self.uncleaned_tiles.discard(vertex)

                directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
                for i, (dx, dy) in enumerate(directions):
                    move_direction = i
                    self.next_pos = (vertex[0] + dx, vertex[1] + dy)
                    print('self.next_pos ', self.next_pos)

                    is_next_pos_x_valid = 0 <= self.next_pos[0] < self.room_width
                    is_next_pos_y_valid = 0 <= self.next_pos[1] < self.room_height

                    is_next_pos_valid = is_next_pos_x_valid and is_next_pos_y_valid and self.next_pos not in self.block_tiles_set and self.next_pos not in self.visited
                    print('is_next_pos_valid ', is_next_pos_valid)
                    if is_next_pos_valid:
                        self.dfs_stack.append((self.next_pos, path + [self.next_pos]))
                        self.came_from[self.next_pos] = vertex
                        return move_direction

        return None



    def set_moving_toward_clean_tile_variables(self):
        print('')
        print('set_moving_toward_clean_tile_variables')
        self.moving_toward_clean_title = True
        self.next_clean_tile = self.find_next_clean_tile(self.pos)
        self.x_iterations_towards_tile, self.y_iterations_towards_tile = self.calculate_moves_to_tile(self.pos, self.next_clean_tile)
        self.total_iterations_towards_tile = abs(self.x_iterations_towards_tile) + abs(self.y_iterations_towards_tile)
        print('current pos, ', self.pos)
        print('next_clean_tile, ', self.next_clean_tile)
        print('x_iterations_towards_tile ', self.x_iterations_towards_tile)
        print('y_iterations_towards_tile ', self.y_iterations_towards_tile)
        print('total_iterations_towards_tile ', self.total_iterations_towards_tile)


    def find_next_clean_tile(self, current_pos):
        print('')
        print('find_next_clean_tile')
        # Start by checking the tiles closest to the current position
        # This list could be shuffled or ordered based on a heuristic

        if not self.uncleaned_tiles:
            print('find_next_clean_tile')
            return None
        print('uncleaned_tiles count ', len(self.uncleaned_tiles))

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
        for dx, dy in directions:
            self.next_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if self.next_pos in self.uncleaned_tiles:
                return self.next_pos

        # If no adjacent clean tile was found, search the entire room
        for tile in self.uncleaned_tiles:
            return tile

        # If all free tiles have been visited or cleaned, there's nowhere left to clean
        return None


    def move_torward_clean_title(self):
        print('')
        print('move_torward_clean_title')
        print('self.pos: ', self.pos)
        print('uncleaned_tiles count ', len(self.uncleaned_tiles))
        move_direction = None
        if not self.uncleaned_tiles:
            return move_direction

        if self.x_iteration_towards_tile < abs(self.x_iterations_towards_tile):
            print('self.x_iterations_towards_tile: ', abs(self.x_iterations_towards_tile))
            print('self.x_iteration_towards_tile: ', self.x_iteration_towards_tile)
            self.x_iteration_towards_tile += 1
            move_left = self.x_iterations_towards_tile < 0
            print('move_left: ', move_left)
            if move_left:
                print('return 3  # Left: ')
                self.last_pos = self.pos
                move_direction = 3 # Left
            else: # move_right
                print('return 1  # Right: ')
                self.last_pos = self.pos
                move_direction = 1  # Right
        elif self.y_iteration_towards_tile < abs(self.y_iterations_towards_tile):
            print('self.y_iterations_towards_tile: ', abs(self.y_iterations_towards_tile))
            print('self.y_iteration_toward_tile: ', self.y_iteration_towards_tile)
            self.y_iteration_towards_tile += 1
            move_down = self.y_iterations_towards_tile > 0
            if move_down:
                print('return 2 # Down: ')
                self.last_pos = self.pos
                move_direction = 2  # Down
            else: # move_up
                print('return 0  # Up: ')
                self.last_pos = self.pos
                move_direction = 0  # Up
        else:
            print('FOUND TARGET TILE')
            self.reset_moving_toward_clean_tile_variables()
            self.dfs_stack = [(self.pos, [self.pos])]
            self.get_next_move(self.pos)

        print('move_direction ', move_direction)
        new_pos = self.new_pos(move_direction, self.pos)
        return move_direction


    def calculate_moves_to_tile(self, pos, target):
        print('')
        print('calculate_moves_to_tile')
        x_distance = target[0] - pos[0]
        y_distance = target[1] - pos[1]
        return x_distance, y_distance


    def reset_moving_toward_clean_tile_variables(self):
        print('')
        print('reset_moving_toward_clean_tile_variables')
        self.moving_toward_clean_title = False
        self.x_iteration_towards_tile = 0
        self.x_iterations_towards_tile = 0
        self.y_iteration_towards_tile = 0
        self.y_iterations_towards_tile = 0
        self.total_iterations_towards_tile = abs(self.x_iterations_towards_tile) + abs(self.y_iterations_towards_tile)


    def new_pos(self, dir, curr_pos):
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


    def get_neighbors(current_pos):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up, right, down, left
        neighbors = []
        for dx, dy in directions:
            next_pos = (current_pos[0] + dx, current_pos[1] + dy)
            neighbors.append(next_pos)
        return neighbors


    def get_random_excluding(input_number):
        if input_number not in [0, 1, 2, 3]:
            raise ValueError("Input number must be 0, 1, 2, or 3")
        numbers = [0, 1, 2, 3]
        numbers.remove(input_number)
        return random.choice(numbers)

    def reset_random_dir(self):
        self.random_dir = {1, 2, 3, 4}
        self.random_dir = set(random.sample(list(self.random_dir), len(self.random_dir)))
        return None