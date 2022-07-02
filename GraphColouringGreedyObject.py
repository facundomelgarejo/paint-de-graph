import execution_time
import samples

class GreedyGraph():
    def __init__(self, initialMatrix):
        self.numberOfVertices = len(initialMatrix)
        self.adjacentMatrix = initialMatrix
        self.adjacentVector = [[] for i in range(self.numberOfVertices)]
        self.paintedGraph = None
        self.colNames = samples.colourNames

    def initAdjacentVector(self):
        for row in range(self.numberOfVertices):
            for colum in range(self.numberOfVertices):
                if self.adjacentMatrix[row][colum] == 1 and colum > row:
                    self.adjacentVector[row].append(colum)
                    self.adjacentVector[colum].append(row) 

    def printPaintedGraph(self):
        for vertex in range(self.numberOfVertices): 
            print("Vertex", vertex, "  ---> ", self.colNames[self.paintedGraph[vertex]])
 
    # Assigns colors (starting from 0) to all
    # vertices and prints the assignment of colors
    # @execution_time.execution_time
    def greedyColoring(self):
        result = [-1] * self.numberOfVertices
    
        # Assign the first color to first vertex
        result[0] = 0;
    
        # A temporary array to store the available colors.
        # True value of available[color] would mean that the
        # color color is assigned to one of its adjacent vertices
        available = [False] * self.numberOfVertices
    
        # Assign colors to remaining V-1 vertices
        for vertex in range(1, self.numberOfVertices):
            
            # Process all adjacent vertices and
            # flag their colors as unavailable
            for adjacent in self.adjacentVector[vertex]: 
                if (result[adjacent] != -1): available[result[adjacent]] = True
    
            # Find the first available color
            color = 0
            while color < self.numberOfVertices:
                if (available[color] == False): break
                color += 1
                
            # Assign the found color
            result[vertex] = color
    
            # Reset the values back to false
            # for the next iteration
            for adjacent in self.adjacentVector[vertex]:
                if (result[adjacent] != -1): available[result[adjacent]] = False

        self.paintedGraph = result


# Python3 program to implement greedy
# algorithm for graph coloring

# 1. Color first vertex with first color. 
# 2. Do following for remaining V-1 vertices. 
# ….. a) Consider the currently picked vertex and color it with the 
# lowest numbered color that has not been used on any previously 
# colored vertices adjacent to it. If all previously used colors 
# appear on vertices adjacent to v, assign a new color to it.

# Analysis of Basic Algorithm 

# The above algorithm doesn’t always use minimum number of colors. Also, the number of colors used sometime 
# depend on the order in which vertices are processed. For example, consider the following two graphs. Note 
# that in graph on right side, vertices 3 and 4 are swapped. If we consider the vertices 0, 1, 2, 3, 4 in left 
# graph, we can color the graph using 3 colors. But if we consider the vertices 0, 1, 2, 3, 4 in right graph, 
# we need 4 colors. 
