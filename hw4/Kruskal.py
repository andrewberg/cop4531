#!/usr/bin/python

import sys
from sys import argv
# Andrew Berg Prim.py for COP4531 due 11/22/16
# open file that is passed in argv[1]

file = open(argv[1], "r") # open file named in argv[1] in read mode

# grab number of nodes
nodeCount = int(file.readline().strip()) # read in number of nodes

# nodecount by nodecount graph storage
graph = [[0 for x in range(nodeCount)] for y in range(nodeCount)]

# read by line and then parse line into lists
edges = [] # empty list
for line in file:
	edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index
for edge in edges:
	node1 = int(edge[0]) # first node of the edge converted to int
	node2 = int(edge[1]) # second node of the edge converted to int
	weight = int(edge[2]) # weight of the edge converted to int

	graph[node1-1][node2-1] = weight # weight of the edge added to graph
	graph[node2-1][node1-1] = weight # make the graph reflective over diag