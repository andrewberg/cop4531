#!/usr/bin/python

import sys
from sys import argv
from collections import defaultdict
# Andrew Berg Kruskal.py for COP4531 due 11/22/16
# open file that is passed in argv[1]

file = open(argv[1], "r") # open file named in argv[1] in read mode

# grab number of nodes
nodeCount = int(file.readline().strip()) # read in number of nodes

class Graph:
    def __init__(self, vertices):
        self.V = vertices # allocate number of verts
        self.graph = [] # dictionary to store all information

    def addEdge(self, u, v, w):
        self.graph.append([u,v,w]) # appends each edge to the graph array

    def find(self, parent, i):
        if parent[i] == i: # if equal to return i
            return i
        return self.find(parent, parent[i]) # continue looking with recursion

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x) # call find on both parents
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        #If ranks are same, then make one as root and increment
        # its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
 
        result = [] #This will store the resultant MST
 
        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]
 
        #Step 1:  Sort all the edges in non-decreasing order of their
        # weight.  If we are not allowed to change the given graph, we
        # can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])
        #print self.graph
 
        parent = [] ; rank = []
 
        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
     
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
 
            # Step 2: Pick the smallest edge and increment the index
            # for next iteration
            u,v,w =  self.graph[i]

            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)
 
            # If including this edge does't cause cycle, include it
            # in result and increment the index of result for next edge
            if x != y:
                e = e + 1  
                result.append([u+1,v+1,w])
                self.union(parent, rank, x, y)          
            # Else discard the edge
        # print
        result = sorted(result, key=lambda a: (a[0], a[1]))

        sumWeight = 0
        for x in result:
        	sumWeight += x[2]
        print(sumWeight)
        for x in result:
        	print "%d %d" % (x[0], x[1])
            
g = Graph(nodeCount)
# read by line and then parse line into lists
edges = [] # empty list
for line in file:
	edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index

for edge in edges:
	g.addEdge(int(edge[0])-1, int(edge[1])-1, int(edge[2]))

g.KruskalMST()



