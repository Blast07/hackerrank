def inversions(orig,left, right):
    global inv
    min_bribes=0
    left_len = len(left)
    right_len = len(right)
    if (left_len>1):
      left_bribes=inversions(left,left[:left_len//2],
                            left[left_len//2:])
      if (left_bribes is not None):
          min_bribes+=left_bribes
      else :return
    if(right_len>1):
      right_bribes+=inversions(right,right[:right_len//2],
                            right[right_len//2:])
      if (right_bribes is not None):
          min_bribes+=right_bribes
      else :return
    left_ind,right_ind,orig_ind=0,0,0
    while(left_ind<left_len and right_ind<right_len):
        if(left[left_ind]>right[right_ind]):
            min_bribes+=left_len - left_ind
            orig[orig_ind] = right[right_ind]
            right_ind+=1
            for x in left[left_ind:]:
                inv[x-1]+=1
                if(inv[x-1]>2):
                    print("Too chaotic")
                    return
        else:
            orig[orig_ind] = left[left_ind]
            left_ind+=1
 
        orig_ind+=1

    if (left_ind==left_len):
        orig[orig_ind:] = right[right_ind:]
    else:
        orig[orig_ind:] = left[left_ind:]
    return min_bribes

def minimumBribes(q):
    min_bribes = inversions(q,q[:len(q)//2],q[len(q)//2:])
    if(min_bribes):
        print(min_bribes)
#def minimumBribes1(q):
#    min_bribes = 0
#    n = len(q)
#    for i in range(n-1,-1,-1):
#        if i+1!=q[i]:
#            if i+1 == q[i-2]:
#                min_bribes+=2
#            elif i+1 == q[i-1]:
#                min_bribes+=1
#            else:
#                if(i+1 not in q[i+1:]):
#                    print("Too chaotic")
#                    return 
#                else:
#                    ind = q.index(i+1)
#                    for j in q[ind+1:]:
#                        if q[ind]>j:
#                            min_bribes+=1
#    print(min_bribes)
#
#def minimumBribes(q):
#    min_bribes=0
#    for i in range(len(q)-1):
#        cur_bribes = 0
#        for j in range(i+1,len(q)):
#            if q[i]>q[j]:
#                cur_bribes+=1
#                if cur_bribes>2:
#                    print("Too chaotic")
#                    return
#        min_bribes+=cur_bribes
#    return min_bribes
#
q = [1,2,5,3,7,8,6,4]
inv = [0 for _ in range(len(q))]
minimumBribes1(q)


