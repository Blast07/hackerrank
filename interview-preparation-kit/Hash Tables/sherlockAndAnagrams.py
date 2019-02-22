def sherlockAndAnagrams(s):
    n = len(s)
    anagram_count = 0
    for i in range(1,n):
        cur_len = i
        anagram_dict = {}
        for j in range(n-cur_len+1):
            cur_str = list(s[j:j+cur_len])
            cur_str.sort()
            cur_str = ''.join(cur_str)
            if(anagram_dict.get(cur_str)):
                anagram_dict[cur_str]+=1
            else:
                anagram_dict[cur_str]=1
            anagram_count += anagram_dict[cur_str]-1
            
    return anagram_count

