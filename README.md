# A star algorithm implementation

### Graph class
Firstly I initialize the picture as a graph
using dictionary. Therefore, I create Graph class. This class has a variable that contain full paths itself
and 3 methods. This variable contains each city as a key and adjacent cities and their distances as a
value in a dictionary.

![alt text](https://duckduckgo.com/?t=ffab&q=arad+bucharest+weighted+graph&iax=images&ia=images&iai=http%3A%2F%2Fi.stack.imgur.com%2FwjrA7.jpg)

Adding edge method that accept 3 arguments, 2 of them are start and end point of the edge, another is
distance that store the edges’ weight.

Make undirected method just creating symmetric connections, for example, from Arad we can go Sibiu,
also from Sibiu we can go Arad.

Get adjacent method accepting 1 parameter (city name). Return other connected cities to city that
passed as an argument.

#### Graph
{'Arad': {'Zerind': 75, 'Sibiu': 140, 'Rimnicu Vilcea': 130, 'Timisoara': 118}, 'Zerind': {'Oradea': 71, 'Arad':
75}, 'Oradea': {'Sibiu': 151, 'Zerind': 71}, 'Sibiu': {'Fagaras': 99, 'Rimnicu Vilcea': 80, 'Arad': 140, 'Oradea':
151}, 'Rimnicu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146, 'Arad': 130}, 'Timisoara': {'Lugoj': 111,
'Arad': 118}, 'Lugoj': {'Mehadia': 70, 'Timisoara': 111}, 'Mehadia': {'Dobreta': 75, 'Lugoj': 70}, 'Dobreta':
{'Craiova': 120, 'Mehadia': 75}, 'Fagaras': {'Bucharest': 211, 'Sibiu': 99}, 'Pitesti': {'Bucharest': 101,
'Rimnicu Vilcea': 97, 'Craiova': 138}, 'Craiova': {'Pitesti': 138, 'Rimnicu Vilcea': 146, 'Dobreta': 120},
'Bucharest': {'Giurgiu': 90, 'Urziceni': 85, 'Fagaras': 211, 'Pitesti': 101}, 'Urziceni': {'Hirsova': 98, 'Vaslui':
142, 'Bucharest': 85}, 'Hirsova': {'Eforie': 86, 'Urziceni': 98}, 'Vaslui': {'Lasi': 92, 'Urziceni': 142}, 'Lasi':
{'Neamt': 87, 'Vaslui': 92}, 'Giurgiu': {'Bucharest': 90}, 'Eforie': {'Hirsova': 86}, 'Neamt': {'Lasi': 87}}

### Node class
This class have name, parent, g, h, f variables. Name is name of city, parent is link between path, g is
g(n) which is real value, h is h(n) is predicted value, f is f(n) = g(n) + h(n).

### Heuristic values
Define a dictionary that contain city name as a key and heuristic values as a value.
#### Heuristic values
{'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77,
'Hirsova': 151, 'Lasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 300, 'Pitesti': 10, 'Rimnicu
Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

## Implementation of A*

### Class Pathfinder

I have a function in a pathfinder class that accept 4 arguments. 1 – full graph, 2 – heuristic
values dictionary, 3 – start city, 4 – goal city.

Firstly, initialize two lists, one of them store not visited cities and another visited cities. Then
creating a start node with start city and goal node with goal city. Then adding start node into
not visited list. After that, start a loop.
<pre>
while opened not empty \
  Find a lowest f value node \
  Add this node into visited list and remove from not visited list \
  If our node is goal node then break the loop \
  Else get adjacent cities of this node // return a dictionary \
  Loop through a dictionary \
    Create adjacent city node \
    If node is visited then continue (prevent infinity loop such as Arad – Sibiu, Sibiu- Arad) \
    Update a f value \
    If a node not in not visited, then add this node into not visited \
</pre>
