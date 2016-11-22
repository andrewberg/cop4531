#!/usr/bin/python

# Andrew Berg Prim.py for COP4531 due 11/22/16

import sys
from sys import argv

def dfs(i):
	j = 0
	visited[i] = 1

	for j in range(nodeCount):
		if (visited[j] == 0 and connectedGraph[i][j]):
			dfs(j)

def findLowest(choose, notIncluded):
	min = sys.maxint # min value to maxint
	index = 0 # min index to 0

	for v in range(nodeCount):
		if (notIncluded[v] == False and choose[v] < min): # check if visited
			min = choose[v] # and if this choice is going to be less
			index = v # sets the index = to the found v
	return index

def buildPairs(conMST, g):
	iterMST = iter(conMST) # skips first element
	next(iterMST) # skip first element
	x = 1 # starts at x =1
	y = []
	for i in iterMST:
		y.append((conMST[x]+1, x+1)) # appends the tuples to y
		x += 1
	y = sorted(y, key=lambda a: (a[0], a[1])) # sorts on a[0] then a[1]
	return y

def printMST(conMST, g):
	iterMST = iter(conMST)
	next(iterMST) # skip first element

	totalCostMST = 0
	x = 1
	for i in iterMST:
		totalCostMST += graph[x][conMST[x]]
		x += 1

	print(totalCostMST) # print size of MST
	pairs = buildPairs(conMST, g) # build pairs based on conMST and g

	for i in pairs:
		print "%d %d" % (i[0], i[1]) # print each pair tup1 then tup2

def buildMST(graph, nodeCount):
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
				conMST[v] = u # find the lowest and set it equal to mst
				choose[v] = graph[u][v] # set the lowest weight for this spot
	
	printMST(conMST, graph)

lines = sys.stdin.readlines() # take all lines from stdin

# grab number of nodes
nodeCount = int(lines[0].strip()) # read in number of nodes

if (nodeCount < 1):
	print("Impossible")
	sys.exit()

del lines[0] # remove first element

# nodecount by nodecount graph storage
graph = [[0 for x in range(nodeCount)] for y in range(nodeCount)]
connectedGraph = [[0 for x in range(nodeCount)] for y in range(nodeCount)]
visited = [0 for x in range(nodeCount)]

# read by line and then parse line into lists
edges = [] # empty list
for line in lines:
	edges.append(line.strip().split(" ")) #strips \n then splits on " "

# populate edges in graph, must subtract 1 from each index
for edge in edges:
	node1 = int(edge[0]) # first node of the edge converted to int
	node2 = int(edge[1]) # second node of the edge converted to int
	weight = int(edge[2]) # weight of the edge converted to int

	connectedGraph[node1-1][node2-1] = 1 # init actual nodes to 1
	graph[node1-1][node2-1] = weight # weight of the edge added to graph
	graph[node2-1][node1-1] = weight # make the graph reflective over diag

"""Call DFS on the 0 vertex to check to make sure connected graph,
	if connected graph then all nodes will be visited by DFS
	from 0 vertex"""

dfs(0)
if (0 in visited):
	print("Impossible")
	sys.exit()

# ------------------------------
# done building graph call Prim()

buildMST(graph, nodeCount)