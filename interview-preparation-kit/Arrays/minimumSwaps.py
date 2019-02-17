def minimumSwaps(arr):
    min_swaps= 0
    i=0
    while(i<len(arr)):
        swap_i = arr[i]-1
        if(i!=swap_i):
            arr[i],arr[swap_i] = arr[swap_i], arr[i]
            min_swaps+=1
        else:
            i+=1
    return min_swaps

arr = [7,1,3,2,4,5,6]
print(minimumSwaps(arr))
