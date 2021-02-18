def exchange(amount, currency):
    exchange = {"MYR": 3.05, "JPY": 79.67,"AUD": 0.97, "IDR": 54.69, "RMB": 4.88, "KRW": 833.02, "TWD": 21.06, "USD": 0.75, "EUR": 0.62, "HKD": 5.85}
    return exchange[currency]*amount

print(exchange(5000, "EUR"))