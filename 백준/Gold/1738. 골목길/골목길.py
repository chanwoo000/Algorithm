import math

def bellman(start_node):
    distances[start_node] = 0

    for _ in range(nodes_count):
        for current_node in range(1, nodes_count + 1):
            for neighbor, weight in adjacency_list[current_node]:
                new_cost = distances[current_node] + weight

                if distances[current_node] != -math.inf and distances[neighbor] < new_cost:
                    distances[neighbor] = new_cost
                    path[neighbor] = current_node

                    if _ == nodes_count - 1:
                        distances[neighbor] = math.inf

if __name__ == "__main__":
    nodes_count, edges_count = map(int, input().split())

    adjacency_list = [[] for _ in range(nodes_count + 1)]
    distances = [-math.inf] * (nodes_count + 1)
    path = [0] * (nodes_count + 1)

    for _ in range(edges_count):
        u, v, w = map(int, input().split())
        adjacency_list[u].append((v, w))

    bellman(1)

    result_path = [nodes_count]

    if distances[nodes_count] != math.inf:
        current_node = nodes_count

        while current_node != 1:
            current_node = path[current_node]
            result_path.append(current_node)

        for node in reversed(result_path):
            print(node, end=" ")
        print()
    else:
        print("-1")
