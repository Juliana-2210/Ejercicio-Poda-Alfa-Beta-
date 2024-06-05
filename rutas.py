class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}  # Diccionario para almacenar vecinos y costos de ruta

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost

def alpha_beta_search(current_node, destination, alpha, beta, path, current_cost, best_path, best_cost, maximizing_player):
    if current_node == destination:
        if current_cost < best_cost:
            best_path[:] = path[:]
            return current_cost
    if maximizing_player:
        value = float('-inf')
        for neighbor, cost in current_node.neighbors.items():
            if cost < beta:
                path.append(neighbor)
                value = max(value, alpha_beta_search(neighbor, destination, alpha, beta, path, current_cost + cost, best_path, best_cost, False))
                alpha = max(alpha, value)
                path.pop()
                if beta <= alpha:
                    break
        return value
    else:
        value = float('inf')
        for neighbor, cost in current_node.neighbors.items():
            if cost < alpha:
                path.append(neighbor)
                value = min(value, alpha_beta_search(neighbor, destination, alpha, beta, path, current_cost + cost, best_path, best_cost, True))
                beta = min(beta, value)
                path.pop()
                if beta <= alpha:
                    break
        return value

# Crear un mapa de carreteras
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')

A.add_neighbor(B, 5)
A.add_neighbor(C, 2)
B.add_neighbor(D, 4)
C.add_neighbor(D, 2)
C.add_neighbor(E, 7)
D.add_neighbor(E, 1)

# Realizar la búsqueda de ruta óptima utilizando poda alfa-beta
origin = A
destination = E
best_path = [origin]
best_cost = alpha_beta_search(origin, destination, float('-inf'), float('inf'), [origin], 0, best_path, float('inf'), True)

# Imprimir la ruta óptima y el costo total
print("Ruta óptima:", ' -> '.join([node.name for node in best_path]))
print("Costo total:", best_cost)
