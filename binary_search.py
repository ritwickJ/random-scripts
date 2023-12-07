import time


def binary_search(A, x):
    
    low = 0
    high = len(A)-1
    
    while high>=low:
        
        mid = (high+low)//2
        
        if A[mid] == x:
            return mid
        
        elif x>A[mid]:
            low = mid+1
            
        else:
            high = mid-1
    
    return -1

def binary_search2(A,x,low,high):

    if not (high>=low):
        return -1
    
    else:
        mid = (low+high)//2
        
        if A[mid] == x:
            return mid
        
        elif x>A[mid]:
            return binary_search2(A, x, mid+1, high)
        else:
            return binary_search2(A, x, low, mid-1)
        
        
def binary_search3(A,x,low,high,ans):
    
    mid = (low+high)//2
    if A[mid] == x:
        ans = mid
        return ans
        
    elif high>=low:
        
        if x>A[mid]:
            ans = binary_search3(A, x, mid+1, high, ans)
        else:
            ans = binary_search3(A, x, low, mid-1, ans)
            
    return ans
            
        

a = [8,10,11,12,100,101,123,155]
x = 155
print(binary_search(a, x)) 
print(binary_search2(a, x, 0, len(a)-1)) 

ans = -1
print(binary_search3(a, x, 0, len(a)-1,ans)) 