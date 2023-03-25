from graph import *
import matplotlib.pyplot as pp


def prob_cycle(num_nodes, num_tests, nodes_per_edge):
    prob_list = []

    for num_edges in range(num_nodes // nodes_per_edge):
        cycle_counter = 0

        for _ in range(num_tests):
            g = create_random_graph(num_nodes, num_edges)
            if has_cycle(g):
                cycle_counter += 1

        prob_list.append(cycle_counter / num_tests)
    return prob_list


n = 100
runs = 100_000
ratio = 2

pp.title('Number of Edges vs Cycle Probability')
pp.plot(prob_cycle(n, runs, ratio))
pp.xlabel('No. of Edges')
pp.ylabel('Cycle Probability')
pp.show()
