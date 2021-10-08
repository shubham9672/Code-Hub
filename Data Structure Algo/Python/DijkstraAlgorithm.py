"""
A python program for Dijkstra's single source shortest path algorithm.
The program is for adjacency list representation of the graph
"""

# Function that implements Dijkstra's single source shortest path algorithm
# for a graph represented using adjacency list representation
def dijkstra(N, graph, src):
    S = list()
    S.append(src)
    dist = {x: 99 for x in range(1, N+1)}
    dist[src] = 0
    minCost = 999
    selected_u = 0
    selected_v = 0

    while S != list(graph.keys()):
        for u in S:
            dictOfu = graph[u]
            for v in dictOfu:
                if v not in S:
                    cost_u_to_v = dist[u] + dictOfu[v]
                    if cost_u_to_v < minCost:
                        minCost = cost_u_to_v
                        selected_u = u
                        selected_v = v
        dist[selected_v] = minCost
        S.append(selected_v)
        print(selected_u, '--->', selected_v)
        minCost = 999
        S.sort()

# Function used to take input of graph and source node
def main():
    graph = {}
    N = int(input('Enter number of Nodes: '))
    for i in range(1, N+1):
        print('Enter adjacent Node(s) and its weight(s) for Node: ', i)
        string = input()
        adjListWithWeights = string.split()
        print(adjListWithWeights)
        adjDict = {}
        for x in adjListWithWeights:
            y = x.split(',')
            adjDict[int(y[0])] = int(y[1])
            graph[i] = adjDict
    print("The input graph is: ", graph)

    src = int(input('Enter source value: '))

    dijkstra(N, graph, src)

# Call the main function to start the program
main()

# Sample program input and output
"""
Suppose the graph is:
        1 ------> 2 (weight 1)
        1 ------> 3 (weight 5)
        2 ------> 1 (weight 1)
        2 ------> 3 (weight 1)
        3 ------> 1 (weight 2)
        3 ------> 2 (weight 2)

The input will be
Enter number of Nodes: 3
Enter adjacent Node(s) and its weight(s) for Node:  1 --------> 2,1 3,5
Enter adjacent Node(s) and its weight(s) for Node:  2 --------> 1,1 3,1
Enter adjacent Node(s) and its weight(s) for Node:  3 --------> 1,2 2,2

The input graph is: -------> {1: {2: 1, 3: 5}, 2: {1: 1, 3: 1}, 3: {1: 2, 2: 2}}

Enter source value: 2

Final output
        2 ---> 1
        2 ---> 3
"""
