def heron_sqrt(n):
    guess = n
    prev_guess = 0
    while round(guess*1000)/1000 != round(prev_guess*1000)/1000:
        prev_guess = guess
        guess = .5*(guess + n/guess)
    return guess

print(heron_sqrt(50))