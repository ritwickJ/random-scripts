import numpy as np

s = "XXXXXXXX_______XX__XX__XX_XX_X_XX______XX__XXX_XX_______XXXXXXXX"

m = []

for c in s:
    if c == 'X':
        m.append(0)
    else:
        m.append(1)
        
m = np.reshape(m, (8,8))
m[1,0] = 0
m[6,7] = 0

def get_dir(p, mv):
    up,down,left,right = 0,0,0,0
    
    #up
    if m[p[0]-1,p[1]] == 1 and mv[p[0]-1,p[1]] < mv[p[0], p[1]]-cost((p[0]-1,p[1])):
        up = 1
    
    #down
    if m[p[0]+1,p[1]] == 1 and mv[p[0]+1,p[1]] < mv[p[0], p[1]]-cost((p[0]+1,p[1])):
        down = 1
    
    #left
    if m[p[0],p[1]-1] == 1 and mv[p[0],p[1]-1] < mv[p[0], p[1]]-cost((p[0],p[1]-1)):
        left = 1
    
    #right
    if m[p[0],p[1]+1] == 1 and mv[p[0],p[1]+1] < mv[p[0], p[1]]-cost((p[0],p[1]+1)):
        right = 1
        
    return up,down,left,right
    
def cost(p):
    return 4 - (m[p[0]+1,p[1]] + m[p[0]-1,p[1]] + m[p[0],p[1]+1] + m[p[0],p[1]-1] )
     
def get_path(p, maze_value, ct):
    
    ct +=1
    
    if p == (1,1):
        return
    
    up,down,left,right = get_dir(p, maze_value)
    
    if up:
        maze_value[p[0]-1, p[1]] = maze_value[p[0], p[1]] - cost( (p[0]-1, p[1]) )

        get_path( (p[0]-1,p[1]),maze_value, ct)
    
    if left:
        maze_value[p[0], p[1]-1] = maze_value[p[0], p[1]] - cost( (p[0], p[1]-1) )

        get_path( (p[0],p[1]-1),maze_value, ct)
        
    if down:
        maze_value[p[0]+1, p[1]] = maze_value[p[0], p[1]] - cost( (p[0]+1, p[1]) )
        
        get_path( (p[0]+1,p[1]),maze_value, ct)
    
    if right:
        maze_value[p[0], p[1]+1] = maze_value[p[0], p[1]] - cost( (p[0], p[1]+1) )
        
        get_path( (p[0],p[1]+1),maze_value, ct)
    

def max_dir(down, up, right, left):
    d = np.argmax([up,down,left,right])
    if d == 0:
        return -1,0
    elif d == 1:
        return 1,0
    elif d == 2:
        return 0,-1
    elif d == 3:
        return 0,1
    
maze_v = np.zeros((8,8))
maze_v[6,6] = 64

print("####################")
#print(maze_v)
print(m)

print("####################")
get_path((6,6), maze_v, 0)

print(maze_v)

ans = np.zeros((8,8))
ans[1,0] = 1
ans[6,7] = 1
r = 1
c = 1
while True:
    ans[r,c] =1
    
    if (r,c) == (6,6):
        break
    dr, dc = max_dir(maze_v[r+1,c], maze_v[r-1,c], maze_v[r,c+1], maze_v[r,c-1])
    r += dr
    c += dc
    
    
print(ans)
    
    
    
    
    