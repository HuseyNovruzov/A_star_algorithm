class Graph:

    def __init__(self):
        self.graph_dict = {}
    
    def add_edge(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
    # for debuging
    def print(self):
        print(self.graph_dict)
    
    def make_undirected(self):
        for name in list(self.graph_dict.keys()):
            for key, value in self.graph_dict[name].items():
                self.graph_dict.setdefault(key, {})[name] = value
    
    def get_adjacent(self, name):
        return self.graph_dict[name]

class Node:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0  

graph = Graph()
# Real values
graph.add_edge('Arad', 'Zerind', 75)
graph.add_edge('Arad', 'Sibiu', 140)
graph.add_edge('Arad', 'Rimnicu Vilcea', 130)
graph.add_edge('Arad', 'Timisoara', 118)

graph.add_edge('Zerind', 'Oradea', 71)
graph.add_edge('Oradea', 'Sibiu', 151)

graph.add_edge('Sibiu', 'Fagaras', 99)
graph.add_edge('Sibiu', 'Rimnicu Vilcea', 80)

graph.add_edge('Rimnicu Vilcea', 'Sibiu', 80)
graph.add_edge('Rimnicu Vilcea', 'Pitesti', 97)
graph.add_edge('Rimnicu Vilcea', 'Craiova', 146)

graph.add_edge('Timisoara', 'Lugoj', 111)
graph.add_edge('Lugoj', 'Mehadia', 70)
graph.add_edge('Mehadia', 'Dobreta', 75)
graph.add_edge('Dobreta', 'Craiova', 120)

graph.add_edge('Fagaras', 'Bucharest', 211)
graph.add_edge('Pitesti', 'Bucharest', 101)
graph.add_edge('Craiova', 'Pitesti', 138)

graph.add_edge('Bucharest', 'Giurgiu', 90)
graph.add_edge('Bucharest', 'Giurgiu', 90)
graph.add_edge('Bucharest', 'Urziceni', 85)

graph.add_edge('Urziceni', 'Hirsova', 98)
graph.add_edge('Hirsova', 'Eforie', 86)
graph.add_edge('Urziceni', 'Vaslui', 142)
graph.add_edge('Vaslui', 'Lasi', 92)
graph.add_edge('Lasi', 'Neamt', 87)

graph.make_undirected()

# Staraight-line distance to Bucharest
heuristics = {}
heuristics['Arad'] = 366
heuristics['Bucharest'] = 0
heuristics['Craiova'] = 160
heuristics['Dobreta'] = 242
heuristics['Eforie'] = 161
heuristics['Fagaras'] = 176
heuristics['Giurgiu'] = 77
heuristics['Hirsova'] = 151
heuristics['Lasi'] = 226
heuristics['Lugoj'] = 244
heuristics['Mehadia'] = 241
heuristics['Neamt'] = 234
heuristics['Oradea'] = 300
heuristics['Pitesti'] = 10
heuristics['Rimnicu Vilcea'] = 193
heuristics['Sibiu'] = 253
heuristics['Timisoara'] = 329
heuristics['Urziceni'] = 80
heuristics['Vaslui'] = 199
heuristics['Zerind'] = 374

    
class PathFinder:
    
    def a_star(graph, line_values, start_city, goal_city):

        # not_visited and visited nodes colleted in these lists
        opened = []
        closed = []
        # initialize start_node
        start_node = Node(start_city, None)
        goal_node = Node(goal_city, None)
        
        opened.append(start_node)

        while len(opened) > 0:
            start_value = float('inf')
            current_node = opened[0]
            # find lowest f cost node
            for node in opened:
                if node.f < start_value:
                    current_node = node
                    start_value = node.f

            # add a node into visited list
            closed.append(current_node)
            # remove visited node from opened list
            opened.remove(current_node)


            if current_node.name == goal_node.name:
                path = []
                while current_node is not None:
                    path.append(f'{current_node.name} : {current_node.g}')
                    current_node = current_node.parent
                print(path[::-1])
                break
            # get adjacent cities
            next_cities = graph.get_adjacent(current_node.name)

            for key, value in next_cities.items():
                
                next_city = Node(key, current_node)

                if next_city in closed:
                    continue

                # Calculate f value
                next_city.g = current_node.g + value
                next_city.h = line_values[next_city.name]
                next_city.f = next_city.g + next_city.h
                # add possible cities into opened
                if next_city not in opened:
                    opened.append(next_city)
        return None

path_finder = PathFinder

path_finder.a_star(graph, heuristics, 'Zerind', 'Bucharest')