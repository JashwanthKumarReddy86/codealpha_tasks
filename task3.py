stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190,
    "META": 500,
    "NFLX": 700,
    "NVDA": 120,
    "INTC": 35,
    "ORCL": 170
}

total = 0

print("================================")
print("     Stock Portfolio Tracker")
print("================================")

print("\nAvailable Stocks:")
for stock in stocks:
    print(stock, "-", stocks[stock])

while True:
    print("\n1. Add Stock")
    print("2. View Total")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ").strip().upper()

        if name in stocks:
            quantity = int(input("Enter quantity: "))

            price = stocks[name]
            value = price * quantity
            total = total + value

            print("\nStock:", name)
            print("Price:", price)
            print("Quantity:", quantity)
            print("Investment:", value)

        else:
            print("Stock not found.")

    elif choice == "2":
        print("\nYour total investment is:", total)

    elif choice == "3":
        print("\nThank you for using the Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")
    file.write("Total Investment: " + str(total))

print("Your result has been saved in portfolio.txt")
