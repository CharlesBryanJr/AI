class Node():

    def __init__(self, parent=None, name=None):
        self.parent = parent
        self.name = name
        self.g = 0  # Actual distance from start node
        self.h = 0  # Heuristic distance to end node
        self.f = 0  # Total cost

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        parent_name = None if self.parent is None else self.parent.name
        return "%s : {%d, %d, %d} parent:%s" % (self.name, self.f, self.g, self.h, parent_name)

def get_distance(road_to_from_list, from_node, to_node):
    for (n1, n2, dist) in road_to_from_list:
        if (n1 == from_node and n2 == to_node) or (n1 == to_node and n2 == from_node):
            return dist
    return None

def get_distance_to_bucharest(geo_distance_to_bucharest_list, node_name):
    for (name, dist) in geo_distance_to_bucharest_list:
        if name == node_name:
            return dist
    return None

def get_children_of_node(node, road_to_from_list):
    children = []
    for (n1, n2, dist) in road_to_from_list:
        if n1 == node.name:
            children.append(Node(node, n2))
        elif n2 == node.name:
            children.append(Node(node, n1))
    return children


def a_star(road_to_from_list, geo_distance_to_bucharest_list, start, end):
    start_node = Node(None, start)
    start_node.g, start_node.h, start_node.f = 0, 0, 0
    end_node = Node(None, end)
    end_node.g, end_node.h, end_node.f = 0, 0, 0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while open_list:
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        children = get_children_of_node(current_node, road_to_from_list)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + get_distance(road_to_from_list, current_node.name, child.name)
            child.h = get_distance_to_bucharest(geo_distance_to_bucharest_list, child.name)
            child.f = child.g + child.h

            if any(child.name == open_node.name and child.g > open_node.g for open_node in open_list):
                continue

            open_list.append(child)



def main():
    geo_distance_to_bucharest_list = [
        ('A', 366),
        ('B', 0),
        ('C', 160),
        ('D', 242),
        ('E', 161),
        ('F', 176),
        ('G', 77),
        ('H', 151),
        ('I', 226),
        ('L', 244),
        ('M', 241),
        ('N', 234),
        ('O', 380),
        ('P', 100),
        ('R', 193),
        ('S', 253),
        ('T', 329),
        ('U', 80),
        ('V', 199),
        ('Z', 374)
    ]

    road_to_from_list = [
        ('A', 'Z', 75),
        ('A', 'T', 118),
        ('A', 'S', 140),
        ('Z', 'O', 71),
        ('S', 'O', 151),
        ('S', 'F', 99),
        ('S', 'R', 80),
        ('T', 'L', 111),
        ('L', 'M', 70),
        ('M', 'D', 75),
        ('D', 'C', 120),
        ('R', 'C', 146),
        ('R', 'P', 97),
        ('F', 'B', 211),
        ('P', 'B', 101),
        ('P', 'C', 138),
        ('B', 'G', 90),
        ('B', 'U', 85),
        ('U', 'H', 98),
        ('H', 'E', 86),
        ('U', 'V', 142),
        ('V', 'I', 92),
        ('I', 'N', 87)
    ]

    start = 'A'
    end = 'B'

    path = a_star(road_to_from_list, geo_distance_to_bucharest_list, start, end)
    print(f'path - {path}')


if __name__ == "__main__":
    main()