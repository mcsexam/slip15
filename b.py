def dls_recursive(node, goal, graph, depth, depth_limit):
    print(node, end=" ")
    if node == goal:
        return True
    if depth == depth_limit:
        return False
    for neighbor in graph.get(node, []):
        if dls_recursive(neighbor, goal, graph, depth + 1, depth_limit):
            return True
    return False

def iddfs(start, goal, graph):
    max_depth = 10
    for depth_limit in range(max_depth):
        print(f"\nSearching at depth limit: {depth_limit}")
        if dls_recursive(start, goal, graph, 0, depth_limit):
            print("\nGoal found!")
            return
    print("\nGoal not found within max depth.")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['K'],
    'G': [],
    'H': [],
    'I': [],
    'K': []
}

start_node = 'A'
goal_node = 'G'
iddfs(start_node, goal_node, graph)
