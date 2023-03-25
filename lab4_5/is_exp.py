from graph import *
from random import randint
from math import factorial


if __name__ == '__main__':
    for i in range(10_000):
        n = randint(2, 10)
        e = randint(0, factorial(n) // (2*factorial(n-2)))
        g = create_random_graph(n, e)
        mis = MIS(g)
        comp_mis = [n for n in g.adj if n not in mis]
        if not is_vertex_cover(g, comp_mis) or len(MVC(g)) != len(comp_mis):
            print('Complement of MIS was not a MVC')
            break
        print('Complement of MIS is a MVC')
    else:
        print('All comparisons were successful')
