function linear(firstTerm, interval, generate) {
    var values = [];
    for (var i = 0; i < generate; i++) {
        values.push(firstTerm + interval*i);
    }
    return values;
}

console.log(linear(14, 5, 60));