class EasyGraph:
    def __init__(self, node_list, undirected=False):
        self.undirected = undirected
        self.node_list = []  # modify depending on cost in node_list

        # if tuple has 3 values, use node_list as data structure
        if len(node_list[0]) == 3:
            self.node_list = node_list
        else:  # no cost, so store 1 as cost
            for node in node_list:
                self.node_list.append(node + (1,))

    def children(self, node):
        children = []
        for tup in self.node_list:
            from_node, to_node, cost = tup
            if from_node == node:
                children.append(to_node)
            if self.undirected and to_node == node:
                children.append(from_node)
        return children

    def cost(self, from_node, to_node):
        for tup in self.node_list:
            tup_from, tup_to, cost = tup
            if from_node == tup_from and to_node == tup_to:
                return cost

        if self.undirected:  # look at reverse
            for tup in self.node_list:
                tup_from, tup_to, cost = tup
                if from_node == tup_to and to_node == tup_from:
                    return cost

if __name__ == "__main__":
    # Test Case 1
    graph1 = EasyGraph([('A', 'B'), ('B', 'C'), ('C', 'D')])
    print("Children of B:", graph1.children('B'))  # Should return ['C']
    print("Cost of A to B:", graph1.cost('A', 'B'))  # Should return 1
    print()

    # Test Case 2
    graph2 = EasyGraph([('A', 'B', 3), ('B', 'C', 5), ('C', 'D', 2)])
    print("Children of B:", graph2.children('B'))  # Should return ['C']
    print("Cost of B to C:", graph2.cost('B', 'C'))  # Should return 5
    print()

    # Test Case 3
    graph3 = EasyGraph([('A', 'B'), ('B', 'C'), ('C', 'D')], undirected=True)
    print("Children of B:", graph3.children('B'))  # Should return ['A', 'C']
    print("Cost of C to B:", graph3.cost('C', 'B'))  # Should return 1
    print()


    # Test Case 4
    graph4 = EasyGraph([('A', 'B', 4), ('B', 'C', 6), ('C', 'D', 3)], undirected=True)
    print("Children of C:", graph4.children('C'))  # Should return ['B', 'D']
    print("Cost of D to C:", graph4.cost('D', 'C'))  # Should return 3
    print()




