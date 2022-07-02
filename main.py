import os
import samples
from GraphColouringBacktrakingObject import BacktrakingGraph
from GraphColouringGreedyObject import GreedyGraph

clearScreen = lambda: os.system("clear") if os.name == "posix" else os.system("cls")

def main():
    clearScreen()

    print (f"Greedy Algorithmic\n")

    greedyGraph = GreedyGraph(samples.graph6_1)
    greedyGraph.initAdjacentVector()
    greedyGraph.greedyColoring()
    greedyGraph.printPaintedGraph()

    print (f"\nBacktraking Algorithmic\n")

    backGraph = BacktrakingGraph(samples.graph6_1)
    backGraph.graphColouring()
    backGraph.filterTheBests()
    backGraph.printPaintedGraph()
    backGraph.showOptimalResults()
    # backGraph.showNopOptimalResults()


# Main module
if __name__ == '__main__': 
    main()
