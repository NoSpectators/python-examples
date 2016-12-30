# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:56:21 2016

@author: John
"""

def GetGraph(arr):
    n = int(arr[0])
    graph = {}
    for i in range(0, n):
        graph[arr[i + 1]] = []
    for i in range(n + 1, len(arr)):
        a, b = arr[i].split('-')
        #print a,b
        graph[a].append(b)
        graph[b].append(a)

    return n, graph
  
def GetPath(node, path):
    res = ''
    while not node is None:
        res = node + '-' + res
        node = path[node]
    return res[:-1]
  
def ShortestPath(arr): 
    n, graph = GetGraph(arr)
    print "n=",n, "graph=",graph
    #print n, graph
    queue = [arr[1]]
    path  = {arr[1] : None}
    while len(queue) > 0:
        cur = queue.pop(0)
        for nxt in graph[cur]:
            if not nxt in path:
                queue.append(nxt)
                path[nxt] = cur
                if nxt == arr[n]:
                    return GetPath(nxt, path)
    return -1
        
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
#first argument n = number of nodes, then comes the nodes, then comes
#the connections between the nodes(edges)
print ShortestPath(["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"])




