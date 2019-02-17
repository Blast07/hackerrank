#import numpy as np
#def arrayManipulations(n,queres):
#    arr = np.zeros((n,),int)
#    for query in queries:
#        a,b,k = *query
#        arr[a:b+1] += k
#    return arr.max()

def arrayManipulation(n,queries):
    arr = [0 for _ in range(n+1)]
    for query in queries:
        a,b,k = query
        arr[a]+=k
        if b+1<=n:arr[b+1]-=k
    max_ = 0
    sum_ = 0 
    for x in arr[1:]:
        sum_+=x
        if max_<sum_:max_=sum_
    return max_

queries = [[1,5,3],[4,8,7],[6,9,1]]
print(arrayManipulations(10,queries))
