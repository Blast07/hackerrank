from collections import defaultdict

def countTriplets(arr,r):
    count = 0
    dict1 ,dict2 =defaultdict(int),defaultdict(int)
    for i arr[-1::-1]
        if i*r in dict2:
            count += dict2[i*r]
        if i*r in dict1:
            dict2[i] += dict1[i*r]
        dict1[i]+=1
    return count
    
print(countTriplets([1,2,2,4,8,8,8,16], 2))

