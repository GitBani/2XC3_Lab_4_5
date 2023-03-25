from graph import *
import matplotlib.pyplot as pp


def prob_connected(num_nodes, num_tests, edges_per_node):
    prob_list = []

    for num_edges in range(edges_per_node * num_nodes):
        connected_counter = 0

        for _ in range(num_tests):
            g = create_random_graph(num_nodes, num_edges)
            if is_connected(g):
                connected_counter += 1

        prob_list.append(connected_counter / num_tests)
    return prob_list


n = 50
runs = 1000
c = 4

pp.title('Number of Edges vs Connected Probability')
pp.plot(prob_connected(n, runs, c))
pp.xlabel('No. of Edges')
pp.xlim(50)
pp.ylabel('Connected Probability')
pp.show()
