from graph import *
import matplotlib.pyplot as pp


def approx_performance_edges():
    ratio = {'approx 1': [], 'approx 2': [], 'approx 3': []}
    for num_edges in range(1, 27, 5):
        sum_mvc = sum_approx1 = sum_approx2 = sum_approx3 = 0
        for _ in range(1000):
            g = create_random_graph(8, num_edges - 1 if num_edges != 1 else num_edges)
            sum_mvc += len(MVC(g))
            sum_approx1 += len(approx1(g))
            sum_approx2 += len(approx2(g))
            sum_approx3 += len(approx3(g))
        ratio['approx 1'].append(sum_approx1 / sum_mvc)
        ratio['approx 2'].append(sum_approx2 / sum_mvc)
        ratio['approx 3'].append(sum_approx3 / sum_mvc)

    return ratio


def approx_performance_nodes():
    ratio = {'approx 1': [], 'approx 2': [], 'approx 3': []}
    for num_nodes in range(4, 16):
        sum_mvc = sum_approx1 = sum_approx2 = sum_approx3 = 0
        for _ in range(500):
            g = create_random_graph(num_nodes, 5)
            sum_mvc += len(MVC(g))
            sum_approx1 += len(approx1(g))
            sum_approx2 += len(approx2(g))
            sum_approx3 += len(approx3(g))
        ratio['approx 1'].append(sum_approx1 / sum_mvc)
        ratio['approx 2'].append(sum_approx2 / sum_mvc)
        ratio['approx 3'].append(sum_approx3 / sum_mvc)

    return ratio


def worst_case():
    ratio = []
    for num_edges in range(1, 11):
        sum_mvc = sum_approx1 = 0
        for _ in range(1000):
            g = create_random_graph(5, num_edges)
            sum_mvc += len(MVC(g))
            sum_approx1 += len(approx1(g))
        ratio.append(sum_approx1 / sum_mvc)

    return ratio


approx_dict = approx_performance_edges()
x = [1, 5, 10, 15, 20, 25]
y1 = approx_dict['approx 1']
y2 = approx_dict['approx 2']
y3 = approx_dict['approx 3']
pp.title('Nodes in Approximation per Nodes in MVC vs Number of Edges')
pp.xlabel('No. of Edges')
pp.ylabel('Ratio of Nodes in Approximation to Nodes in MVC')
pp.plot(x, y1)
pp.plot(x, y2)
pp.plot(x, y3)
pp.legend(['Approx 1', 'Approx 2', 'Approx 3'])
pp.show()


approx_dict = approx_performance_nodes()
x = [i for i in range(4, 16)]
y1 = approx_dict['approx 1']
y2 = approx_dict['approx 2']
y3 = approx_dict['approx 3']
pp.title('Nodes in Approximation per Nodes in MVC vs Number of Nodes')
pp.xlabel('No. of Nodes')
pp.ylabel('Ratio of Nodes in Approximation to Nodes in MVC')
pp.plot(x, y1)
pp.plot(x, y2)
pp.plot(x, y3)
pp.legend(['Approx 1', 'Approx 2', 'Approx 3'])
pp.show()


y = worst_case()
x = [i for i in range(1, 11)]
pp.title('Nodes in Approximation per Nodes in MVC For All Graphs of 5 Nodes')
pp.xlabel('No. of Edges')
pp.ylabel('Ratio of Nodes in Approximation to Nodes in MVC')
pp.plot(x, y)
pp.show()
