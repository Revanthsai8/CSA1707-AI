# Map Colouring using CSP

# Define regions and their neighbours
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colours
colors = ['Red', 'Green', 'Blue']

# Store assigned colours
color_map = {}

# Check whether a colour is safe
def is_safe(region, color):
    for neighbour in graph[region]:
        if neighbour in color_map and color_map[neighbour] == color:
            return False
    return True

# CSP Backtracking algorithm
def map_coloring(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_safe(region, color):
            color_map[region] = color

            if map_coloring(regions[1:]):
                return True

            del color_map[region]

    return False

# Main program
if map_coloring(list(graph.keys())):
    print("Map Coloring Solution:")
    for region, color in color_map.items():
        print(region, ":", color)
else:
    print("No solution exists")
