from collections import deque

# =========================
# LINKED LIST
# =========================
class CityNode:
    def __init__(self, city):
        self.city = city
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_city(self, city):
        new_node = CityNode(city)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def get_cities(self):
        cities = []
        temp = self.head

        while temp:
            cities.append(temp.city)
            temp = temp.next

        return cities


# =========================
# STACK
# =========================
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items[::-1]


# =========================
# QUEUE
# =========================
class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.popleft()

    def get_items(self):
        return list(self.items)


# =========================
# GRAPH
# =========================
class Graph:
    def __init__(self):
        self.graph = {}

    def add_city(self, city):
        if city not in self.graph:
            self.graph[city] = []

    def connect_city(self, c1, c2):
        if c1 in self.graph and c2 in self.graph:
            self.graph[c1].append(c2)
            self.graph[c2].append(c1)

    def get_graph(self):
        return self.graph

    # BFS for route finding
    def bfs(self, start, end):
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == end:
                return path

            if node not in visited:
                visited.add(node)

                for neighbor in self.graph.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return []