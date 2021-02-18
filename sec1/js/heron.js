function heronSqrt(n) {
    var guess = n, prevGuess = 0;
    while (guess.toFixed(3) != prevGuess.toFixed(3)) {
        prevGuess = guess;
        guess = .5*(guess + n/guess);
    }
    return guess;
}

console.log(heronSqrt(50));