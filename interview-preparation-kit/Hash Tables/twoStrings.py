"""
    Both the functions work(full points on hackerrank)
    however second functions is faster
"""
def twoStrings(s1, s2):
    if any([ch in s2 for ch in s1]):
        return "YES"
    else:
        return "NO":

def twoStrings2(s1,s2):
    s1 = set(s1)
    s2 = set(s2)
    if(s1.intersection(s2)):
        return "YES"
    else:
        return "NO"


