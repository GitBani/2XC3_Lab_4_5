from collections import deque
from random import randint


# Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def print(self):
        print(self.adj)

    def get_size(self):
        return len(self.adj)


# Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1: True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False


# Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if marked[node]:
                    continue
                if node == node2:
                    return True
                S.append(node)
    return False


def BFS2(g, start_node, end_node):
    marked = set()
    q = [(start_node, [start_node])]

    while q:
        curr_node, path = q.pop(0)

        if curr_node == end_node:
            return path

        if curr_node in marked:
            continue

        marked.add(curr_node)
        for adj_node in g.adj[curr_node]:
            if adj_node not in marked:
                new_path = path + [adj_node]
                q.append((adj_node, new_path))

    return []


def DFS2(g, start_node, end_node):
    marked = set()
    s = [(start_node, [start_node])]

    while s:
        curr_node, path = s.pop()

        if curr_node == end_node:
            return path

        if curr_node in marked:
            continue

        marked.add(curr_node)
        for adj_node in g.adj[curr_node]:
            if adj_node not in marked:
                new_path = path + [adj_node]
                s.append((adj_node, new_path))

    return []


def BFS3(g, start_node):
    marked = set()
    q = [start_node]
    pred_dict = {}

    while q:
        curr_node = q.pop(0)

        if curr_node in marked:
            continue

        marked.add(curr_node)
        for adj_node in g.adj[curr_node]:
            if adj_node not in marked and adj_node not in pred_dict:
                pred_dict[adj_node] = curr_node
                q.append(adj_node)

    return pred_dict


def DFS3(g, start_node, marked, pred_dict):
    marked.add(start_node)
    for adj_node in g.adj[start_node]:
        if adj_node not in marked and adj_node not in pred_dict:
            pred_dict[adj_node] = start_node
            DFS3(g, adj_node, marked, pred_dict)

    return pred_dict


def has_cycle(g):
    for node in g.adj:
        if dfs_for_has_cycle(g, node, node):
            return True

    return False


def dfs_for_has_cycle(g, node1, node2):
    s = [node1]
    marked = set()
    # to avoid hopping back to previous node
    prev_node = None

    while s:
        current_node = s.pop()
        if current_node not in marked:
            marked.add(current_node)

            for node in g.adj[current_node]:
                if node == node2 and node != prev_node:
                    return True
                s.append(node)

        prev_node = current_node
    return False


def is_connected(g):
    for node in g.adj:
        if not BFS3(g, node):
            return False

    return True


# assumes possible graph
def create_random_graph(i, j):
    g = Graph(i)

    for edge in range(j):
        n1 = randint(0, i-1)
        n2 = randint(0, i-1)

        while g.are_connected(n1, n2) or n1 == n2:
            n1 = randint(0, i - 1)
            n2 = randint(0, i - 1)

        g.add_edge(n1, n2)

    return g


def find_path(d, end_node, start_node):
    curr_node = end_node
    path = [curr_node]
    while curr_node != start_node:
        curr_node = d.get(curr_node)
        path.append(curr_node)
    return path


# Use the methods below to determine minimum vertex covers

def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy


def power_set(set):
    if not set:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])


def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not (start in C or end in C):
                return False
    return True


def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


def remove_incident_edges(adj_list, node_to_remove):
    adj_list[node_to_remove] = []
    for key in adj_list:
        if node_to_remove not in adj_list[key]:
            continue
        adj_list[key].remove(node_to_remove)


def approx1(g):
    c = []
    adj_list = {key: val[:] for key, val in g.adj.items()}

    for _ in range(len(adj_list)):
        v = max(adj_list, key=lambda k: len(adj_list[k]))
        c.append(v)
        remove_incident_edges(adj_list, v)

        if is_vertex_cover(g, c):
            return c


def approx2(g):
    c = []
    adj_list = {key: val[:] for key, val in g.adj.items()}

    for _ in range(len(adj_list)):
        v = randint(0, len(adj_list) - 1)
        while v in c:
            v = randint(0, len(adj_list) - 1)
        c.append(v)

        if is_vertex_cover(g, c):
            return c


def approx3(g):
    c = []
    adj_list = {key: val[:] for key, val in g.adj.items()}

    for _ in range(len(adj_list)):
        u = randint(0, len(adj_list) - 1)
        v = randint(0, len(adj_list) - 1)
        while u == v or u in c:
            u = randint(0, len(adj_list) - 1)
        while v == u or v in c:
            v = randint(0, len(adj_list) - 1)

        c.append(u)
        c.append(v)
        remove_incident_edges(adj_list, u)
        remove_incident_edges(adj_list, v)

        if is_vertex_cover(g, c):
            return c


def is_independent_set(g, s):
    for node in s:
        for adj_node in g.adj[node]:
            if adj_node in s:
                return False
    return True


def MIS(g):
    nodes = [i for i in range(g.get_size())]
    subsets = power_set(nodes)
    max_is = []
    for subset in subsets:
        if is_independent_set(g, subset):
            if len(subset) > len(max_is):
                max_is = subset
    return max_is
