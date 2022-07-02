# Python3 program to implement greedy
# algorithm for graph coloring
 
def add_edge(adjacents, vertex1, vertex2):
    # Note: the graph is undirected
    adjacents[vertex1].append(vertex2)
    adjacents[vertex2].append(vertex1) 
    return adjacents
 
# Assigns colors (starting from 0) to all
# vertices and prints the assignment of colors
def greedy_coloring(adjacents, number_of_vertices):
    result = [-1] * number_of_vertices
 
    # Assign the first color to first vertex
    result[0] = 0;
 
 
    # A temporary array to store the available colors.
    # True value of available[color] would mean that the
    # color color is assigned to one of its adjacent vertices
    available = [False] * number_of_vertices
 
    # Assign colors to remaining V-1 vertices
    for vertex in range(1, number_of_vertices):
         
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for adjacent in adjacents[vertex]: 
            if (result[adjacent] != -1): available[result[adjacent]] = True
 
        # Find the first available color
        color = 0
        while color < number_of_vertices:
            if (available[color] == False): break
            color += 1
             
        # Assign the found color
        result[vertex] = color
 
        # Reset the values back to false
        # for the next iteration
        for adjacent in adjacents[vertex]:
            if (result[adjacent] != -1): available[result[adjacent]] = False
 
    # Print the result
    for vertex in range(number_of_vertices): print("Vertex", vertex, " --->  Color", result[vertex])


def main():
    graph1 = [  [0,1,0,0,0,0,0,0,0,0],
                [1,0,1,0,1,0,0,0,0,0],
                [0,1,0,1,0,0,0,0,0,0],
                [0,0,1,0,1,0,1,0,0,0],
                [0,1,0,1,0,1,0,0,0,0],
                [0,0,0,0,1,0,1,1,0,1],
                [0,0,0,1,0,1,0,1,0,0],
                [0,0,0,0,0,1,1,0,1,0],
                [0,0,0,0,0,0,0,0,1,1],
                [0,0,0,0,0,1,0,0,1,0]]

    g1 = [[] for i in range(10)]
    for row in range(10):
        for colum in range(10):
            if graph1[row][colum] == 1 and colum > row: add_edge(g1, row, colum)

    greedy_coloring(g1, 10)

 
 
# Driver Code
if __name__ == '__main__':
    main()
     
 
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
