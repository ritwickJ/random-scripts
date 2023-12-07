import heapq
import math


def make_dict(A,N,M):
    m = 0
    for a in A:
        temp = max(a)
        if temp>m:
            m = temp
            
    dict_graph = {}

    for i in range(N):
        for j in range(M):
            nodes = []
            if i+1 < N:
                nodes.append((i+1)*M+j)
            if j+1 < M:
                nodes.append( i*M +j+1 )
                
            dict_graph[j+i*M] = (m-A[i][j],nodes)
    
    return dict_graph

def dijkstra(graph):
    start = 0
    
    minheap = []
    heapq.heapify(minheap)
    
    dist = [math.inf]*len(graph)
    prev = [None]*len(graph)
    visited = [False]*len(graph)
    
    dist[start] = graph[0][0]
    heapq.heappush(minheap, (graph[0][0],start))
    
    while minheap:
        
        node = heapq.heappop(minheap)
        curDist = node[0]
        curNode = node[1]
        
        if visited[curNode]:
            continue
        visited[curNode] = True
        
        neighbors = graph[curNode][1]
        for nextNode in neighbors:
            
            nextDist = curDist + graph[nextNode][0]
            if nextDist<dist[nextNode]:
                dist[nextNode] = nextDist
                prev[nextNode] = curNode
                heapq.heappush(minheap, (nextDist, nextNode))
                
    return dist,prev
    

def solution(A):
    N = len(A)
    M = len(A[0])
    
    g = make_dict(A, N, M)
    d,p = dijkstra(g)
    
    pos = p[len(A)*len(A[0])-1]
    points = A[N-1][M-1]
    
    while True:
        points += A[pos//M][pos%M]
        if pos:
            pos = p[pos]
        else:
            break    
    
    return points

A = [[2,2,4,2],[0,3,0,1],[1,2,2,1],[4,1,2,2]]
print(solution(A))




