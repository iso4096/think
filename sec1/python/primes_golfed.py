def p(n=100,r=[]):
    for i in range(1,n+1):
        if all(i%e for e in r) and i-1:r+=[i]
    return r

print(p())