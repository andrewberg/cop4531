#!/usr/bin/python

# Andrew Berg Kruskal.py for COP4531 due 11/22/16

import sys
from sys import argv

lines = sys.stdin.readlines() # take all lines from stdin

# grab number of nodes
nodeCount = int(lines[0].strip()) # read in number of nodes
del lines[0] # remove first element that was already read in

class Edge:
    def __init__(self, src, des, w):
        self.src = src
        self.des = des
        self.w = w

class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes # allocate number of verts
        self.graph = [] # dictionary to store all information

    def addEdge(self, src, des, w):
        self.graph.append(Edge(src, des, w)) 
        # appends each edge to the graph array

    def find(self, subsets, i):
        if subsets[i].parent == i: # if equal to return i
            return i
        return self.find(subsets, subsets[i].parent) # continue looking with recursion

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

            if x != y: # make sure it does not cause an edge to be acycle
                e += 1
                result.append(Edge(src+1, des+1 , w)) # inc src and des to display
                self.isUnion(sets, x, y)  
       
        # print
        result = sorted(result, key=lambda a: (a.src, a.des))

        sumWeight = 0
        for x in result:
        	sumWeight += x.w # x[2] is the weight
        print(sumWeight) # print the sumWeight after summing all weights
        
        for x in result:
        	print "%d %d" % (x.src, x.des) # print out all the edges in order
            
g = Graph(nodeCount)
# read by line and then parse line into lists
edges = [] # empty list
for line in lines:
	edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index

for edge in edges:
	g.addEdge(int(edge[0])-1, int(edge[1])-1, int(edge[2]))

g.KruskalMST()