function generatePrimes(no=100) {
    var primes = [];
    for (var i = 1; i <= no; i++) {
        if (i !== 1) {
            isPrime = true;
            for (var j = 0; j < primes.length; j++) {
                if (i % primes[j] == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                primes.push(i);
            }
        }
    }

    return primes;
}

console.log(generatePrimes());