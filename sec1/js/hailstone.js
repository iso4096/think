function hailstone(n) {
    var seq = [n];
    while (n != 1) {
        if (n%2) {
            n = 3*n+1;
        } else {
            n /= 2;
        }
        seq.push(n)
    }
    return seq;
}

console.log(hailstone(200));