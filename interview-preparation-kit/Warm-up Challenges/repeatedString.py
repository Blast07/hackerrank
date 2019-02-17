def counta(string, n):
    num_a =0
    for i in range(n):
        if string[i]=='a':num_a+=1
    return num_a

def repeatedString(string, n):
    size = len(string)
    num_a = counta(string,size)
    if(size==n):return num_a
    elif(size>n):
        num_a = counta(string,n)
        return num_a;
    else:
        remainder = n%size
        tot_num_a = num_a*(n//size) + counta(string,remainder)
        return tot_num_a
 
print(repeatedString("abaa",15))
