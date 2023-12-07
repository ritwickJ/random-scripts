import heapq
import math

def make_dict(A,N,M):
    dict_graph = {}

    for i in range(N):
        for j in range(M):
            nodes = []
            if i+1 < N:
                nodes.append((i+1)*M+j)
            if j+1 < M:
                nodes.append( i*M +j+1 )
                
            dict_graph[j+i*M] = (A[i][j],nodes)
    
    return dict_graph

def explore(p,graph,points,end, point_list):
    
    nodes = graph[p][1]
    right = None
    down = None
    
    if len(nodes) == 2:
        down = nodes[0]
        right = nodes[1]
    
    elif nodes: 
        down = nodes[0]
    
    points += graph[p][0]
    
    if p == end:
        point_list.append(points)
        return
    
    if down:
        
        explore(down,graph,points,end,point_list)
        
    if right:
        explore(right,graph,points,end,point_list)
        
    return

def solution(A):
    # write your code in Python 3.6
    
    # make dict of nodes, the points and connections
    g = make_dict(A, len(A), len(A[0]))
    l = []
    explore(0,g,0,len(A)*len(A[0])-1,l)
    
    return max(l)

A = [[2,2,4,2],[0,3,0,1],[1,2,2,1],[4,1,2,2]]
print(solution(A))




