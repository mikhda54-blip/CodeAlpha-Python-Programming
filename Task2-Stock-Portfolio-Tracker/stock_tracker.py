# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

portfolio = {}
total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()

    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = qty
    else:
        print("Stock not found")

print("\nPortfolio Summary")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total += investment

    print(stock, "=", investment)

print("\nTotal Investment =", total)

# Save to file
file = open("summary.txt", "w")

file.write("Portfolio Summary\n")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty

    file.write(f"{stock} = {investment}\n")

file.write(f"\nTotal Investment = {total}")

file.close()

print("\nData saved in summary.txt")