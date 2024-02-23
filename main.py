itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00 

# Calculating profit (profit) as the retail price minus the wholesale price
profit = retailPrice - wholesalePrice

# Calculate the sale price (salePrice) as 25 percent deducted from the retail price
discountPercentage = 0.25 # 25% discount
salePrice = retailPrice * (1 - discountPercentage)

# Calculate the profit when the salePrice is used (saleProfit) as the salePrice minus
# the wholesalePrice
saleProfit = salePrice - wholesalePrice 

# Printing the results
print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))

