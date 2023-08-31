import igraph
import time
import sys

def f(n):

    start = round(time.time(),6)
    n = int(n)

    size = int(n)
    graph = igraph.Graph.Barabasi(size, size)

    result = graph.spanning_tree(None, False)
    end = round(time.time(),6)

if __name__ == "__main__":
    event = sys.argv[1]
    f(event)