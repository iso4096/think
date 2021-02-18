function exchange(amount, currency) {
    var prices = {"MYR": 3.05, "JPY": 79.67,"AUD": 0.97, "IDR": 54.69, "RMB": 4.88, "KRW": 833.02, "TWD": 21.06, "USD": 0.75, "EUR": 0.62, "HKD": 5.85};
    return prices[currency]*amount;
}

console.log(exchange(5000, "EUR"));