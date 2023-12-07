import heapq
import math

def get_neighbors(node, graph):
    temp = []
    for i,n in enumerate(graph[node]):
        if n > 0:
            temp.append(i) 
    return temp

def dijkstra(start, graph):
    minheap = []
    heapq.heapify(minheap)
    
    dist = [math.inf]*len(graph)
    prev = [None]*len(graph)
    visited = [False]*len(graph)
    
    dist[start] = 0
    heapq.heappush(minheap, (0,start))
    
    while minheap:
        
        node = heapq.heappop(minheap)
        curDist = node[0]
        curNode = node[1]
        
        if visited[curNode]:
            continue
        visited[curNode] = True
        
        neighbors = get_neighbors(curNode, graph)
        for nextNode in neighbors:
            
            nextDist = curDist + graph[curNode][nextNode]
            if not visited[nextNode] and nextDist<dist[nextNode]:
                dist[nextNode] = nextDist
                prev[nextNode] = curNode
                heapq.heappush(minheap, (nextDist, nextNode))
                
    return dist,prev,visited

graph = [[0,7,9,14],[-1,0,10,-1],[-1,-1,0,2],[-1,-1,-1,0]]
start = 0

print(dijkstra(start, graph))
            
