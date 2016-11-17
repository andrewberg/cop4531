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

def findLowest(choose, notIncluded):
	min = sys.maxint # min value to maxint
	min_index = 0 # min index to 0

	for v in range(nodeCount):
		if (notIncluded[v] == False and choose[v] < min):
			min = choose[v]
			min_index = v
	return min_index

def printMST(conMST, g):
	iterMST = iter(conMST)
	next(iterMST) # skip first element
	print(len(conMST) - 1) # print size of MST

	x = 1
	for i in iterMST:
		print "%d %d %d" % (conMST[x], x, graph[x][conMST[x]])
		x += 1

conMST = [0 for x in range(nodeCount)] # init all values to 0
choose = [sys.maxint for x in range(nodeCount)] # init all values to 0
notIncluded = [False] * nodeCount # init all vertices to not visited

conMST[0] = -1 # set the root of the MST
choose[0] = 0 # make 0 so this is the first vertex being chosen

for vCount in range(nodeCount): # iterate over all the vertices
	# pick the minimum choose vertex from the set of verts not in MST
	u = findLowest(choose, notIncluded)
	
	notIncluded[u] = True # add the picked vertex to the notIncluded

	for v in range(nodeCount):
		if (graph[u][v] and notIncluded[v] == False and graph[u][v] < choose[v]):
			conMST[v] = u
			choose[v] = graph[u][v]

printMST(conMST, graph)





