#!/usr/bin/python

# Andrew Berg Kruskal.py for COP4531 due 11/22/16

import sys
from sys import argv

"""Psuedocode
    1. for each node v of G, make the empty set out of v
    2. Sort the edge of G in ascending order
    3. Take the union of x and y and if they belong to different sets,
       add to the result MST"""

def dfs(i):
    visited[i] = 1 # mark the ith vertice as visited
    for j in range(nodeCount):
        if (visited[j] == 0 and connectedGraph[i][j]):
            dfs(j)

"""Edge class to fill the Graph class full of Edges"""
class Edge:
    def __init__(self, src, des, w):
        self.src = src
        self.des = des
        self.w = w

"""Subset class to be used with isUnion in Graph class for
    tracking purposes"""
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

"""General Graph class for Python with Union and Kruskal MST
    algorithmic ability added"""
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes # allocate number of verts
        self.graph = [] # dictionary to store all information

    def addEdge(self, src, des, w):
        self.graph.append(Edge(src, des, w)) 
        # appends each edge to the graph array

    """General Python funciton to find a parent, simliar to what
        is used in other implementation of the Kruskal algo."""
    def find(self, subsets, i):
        if subsets[i].parent == i: # if equal to return i
            return i
        return self.find(subsets, subsets[i].parent) # continue looking with recursion
    
    """General Python helper function that uses subsets of parent 
        and rank to find whether it is a union.  This function is
        similiar to others found online"""
    def isUnion(self, subsets, x, y):
        xVal = self.find(subsets, x) # call find on both parents
        yVal = self.find(subsets, y)
 
        if subsets[xVal].rank < subsets[yVal].rank:
            subsets[xVal].parent = yVal
        elif subsets[xVal].rank > subsets[yVal].rank:
            subsets[yVal].parent = xVal
        else:
            subsets[xVal].rank += 1
            subsets[yVal].parent = xVal

    def KruskalMST(self):
        result = [] # use this to build the MST
        sets = []   # use this to store class Subset instances
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        # goes through all the values based on weight from to least to
        # greatest
        self.graph = sorted(self.graph, key=lambda a: a.w)

        # goes through and creates trees based on each node of the graph
        # for each node make the empty set of 0
        for node in range(self.nodes):
            sets.append(Subset(node, 0))
     
        # loop through the edges all except for one
        while e < self.nodes - 1:
            src = self.graph[i].src
            des = self.graph[i].des
            w   = self.graph[i].w

            x = self.find(sets, src) 
            y = self.find(sets, des)
            i += 1

            """If x and y belogn to different sets, add (u,v) to result
                tree"""
            if x != y: # make sure it does not cause an edge to be acycle
                e += 1
                result.append(Edge(src+1, des+1 , w)) # inc src and des to display
                self.isUnion(sets, x, y)  
       
        # print
        result = sorted(result, key=lambda a: (a.src, a.des))

        sumWeight = 0
        for x in result:
            sumWeight += x.w # x.w is the weight
        print(sumWeight) # print the sumWeight after summing all weights
        
        for x in result:
            print "%d %d" % (x.src, x.des) # print out all the edges in order

file = open(argv[1], "r") # open file named in argv[1] in read mode

# grab number of nodes
nodeCount = int(file.readline().strip()) # read in number of nodes

if (nodeCount < 1):
    print("Impossible")
    sys.exit()

"""Setup the values for the graph and the DFS check for
    connectivity"""           
g = Graph(nodeCount)
connectedGraph = [[0 for x in range(nodeCount)] for y in range(nodeCount)]
visited = [0 for x in range(nodeCount)]

# read by line and then parse line into lists
edges = [] # empty list
for line in file:
    edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index
for edge in edges:
    g.addEdge(int(edge[0])-1, int(edge[1])-1, int(edge[2]))
    connectedGraph[int(edge[0])-1][int(edge[1])-1] = 1

"""Call DFS on the 0 vertex to check to make sure connected graph,
    if connected graph then all nodes will be visited by DFS
    from 0 vertex"""

dfs(0)
if (0 in visited):
    print("Impossible")
    sys.exit()

g.KruskalMST()