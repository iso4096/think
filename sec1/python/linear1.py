def linear(first_term, interval, generate):
    vals = []
    for i in range(generate):
        vals.append(first_term + interval*i)
    return vals

print(linear(14, 5, 60))