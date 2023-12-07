def optimal_count(v,x):
    count = 0
    while True:
    
        if v//2 <= x:
            count += v-x
            break
        
        elif v%2 == 1:
            v -= 1
            count +=1
            
        v = v//2
        count += 1
        
    return count


def double_it(l):
    
    for i in range(len(l)):
        l[i] *= 2
        
    return l

# given a target lis [4,6,10,11,3]
# operations :- increment each
#                double all
#                double each
#
#return the number of operations needed to reach target from [0,0,0,0]

def solution(target):
    
    count = 0
    basket = [0]*len(target)
    min_pos = target.index(min(target))
    
    # increment to 1
    for i,v in enumerate(target):
        if v>0:
            basket[i] = 1
            count += 1
         
    # double everything
    while True:
        if target[min_pos] < 2*basket[min_pos] or target[min_pos] == 0:
            break
        
        basket = double_it(basket)
        count += 1
        
    # count individual optimals now
    for i in range(len(target)):
        count += optimal_count(target[i], basket[i])
        
    return count


print(solution([0,6]))
        

        
            