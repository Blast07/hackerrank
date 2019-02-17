def sockMerchant(n, socks):
    pairs = {}
    for sock in socks:
        if(pairs.get(sock)):
            pairs[sock] +=1
        else: pairs[sock] =1
    total = 0
    for n in pairs.values():
        total += n//2
    return total
