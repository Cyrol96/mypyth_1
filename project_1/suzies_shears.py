# Data lists
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the average haircut price
total_price = sum(prices)
average_price = total_price / len(prices)
print("Average Haircut Price:", average_price)

# Calculate new prices after a $5 discount
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculate total revenues
total_revenue = sum(prices[i] * last_week[i] for i in range(len(hairstyles)))
print("Total Revenue:", total_revenue)

# Calculate average daily revenue
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# Find haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Haircuts under $30:", cuts_under_30)
