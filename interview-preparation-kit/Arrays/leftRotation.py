def rotLeft(a, d):
    copy_a = a[:]
    for i in range(len(a)):
        a[i-d] = copy_a[i] 
    return a

print(rotLeft([1,2,3,4,5],2))
