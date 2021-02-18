def hailstone(n):
    seq = [n]
    while n != 1:
        if n%2:
            n = 3*n+1
        else:
            n //= 2
        seq.append(n)
    return seq

print(hailstone(200))