def countingValleys(n, steps):
    level = 0
    valleys = 0
    for step in steps:
        if step == 'U':
            level +=1
            if level==0:valleys+=1
        else:
            level -= 1
    return valleys
