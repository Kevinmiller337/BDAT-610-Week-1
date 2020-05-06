print(" As of 5/5/2020 at 12:00 am, bitcoin is currently trading at $9005.89 per bitcoin.")
bitcoinExchangeRate = 9009.89
userBitcoinAmount = float(input("Enter your bitcoin amount: "))
totalValue = userBitcoinAmount * bitcoinExchangeRate
print(" That is worth", totalValue, "us dollars")
