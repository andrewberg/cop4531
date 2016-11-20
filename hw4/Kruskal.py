#!/usr/bin/python

# Andrew Berg Kruskal.py for COP4531 due 11/22/16

import sys
from sys import argv

lines = sys.stdin.readlines() # take all lines from stdin

# grab number of nodes
nodeCount = int(lines[0].strip()) # read in number of nodes
del lines[0] # remove first element that was already read in

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes # allocate number of verts
        self.graph = [] # dictionary to store all information

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w]) # appends each edge to the graph array

    def find(self, parent, i):
        if parent[i] == i: # if equal to return i
            return i
        return self.find(parent, parent[i]) # continue looking with recursion

    def isUnion(self, parent, rank, x, y):
        xVal = self.find(parent, x) # call find on both parents
        yVal = self.find(parent, y)
 
        if rank[xVal] < rank[yVal]:
            parent[xVal] = yVal
        elif rank[xVal] > rank[yVal]:
            parent[yVal] = xVal
        else:
            parent[yVal] = xVal
            rank[xVal] += 1

    def KruskalMST(self):
        result = [] # use this to build the MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

        # goes through all the values based on weight from to least to
        # greatest
        self.graph = sorted(self.graph, key=lambda a: a[2])
 
        parent = [] ; rank = []
 
        # goes through and creates trees based on each node of the graph
        for node in range(self.nodes):
            parent.append(node)
            rank.append(0)
     
        # loop through the edges all except for one
        while e < self.nodes - 1:
            u,v,w = self.graph[i]

            x = self.find(parent, u) 
            y = self.find(parent, v)
            i += 1

            if x != y: # make sure it does not cause an edge to be acycle
                e += 1
                result.append([u+1,v+1,w]) # increment u and v to display
                                           # correctly at end
                self.isUnion(parent, rank, x, y)  
       
        # print
        result = sorted(result, key=lambda a: (a[0], a[1]))

        sumWeight = 0
        for x in result:
        	sumWeight += x[2] # x[2] is the weight
        print(sumWeight)
        for x in result:
        	print "%d %d" % (x[0], x[1]) # print out all the edges in order
            
g = Graph(nodeCount)
# read by line and then parse line into lists
edges = [] # empty list
for line in lines:
	edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index

for edge in edges:
	g.addEdge(int(edge[0])-1, int(edge[1])-1, int(edge[2]))

g.KruskalMST()