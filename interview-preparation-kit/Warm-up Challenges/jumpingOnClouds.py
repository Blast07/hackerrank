def jumpingOnClouds(clouds):
    min_steps = 0
    n = len(clouds)
    i = 0
    while(i<n-1):
        if clouds[i]==0:
            if (i+2<n and clouds[i+2]==0):
                i+=2
            elif(i+1<n and clouds[i+1]==0):
                i+=1
            min_steps+=1
    return min_steps

print(jumpingOnClouds([0,0,1,0,0,1,0]))
    

    
