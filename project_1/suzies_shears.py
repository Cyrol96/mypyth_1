# List of available hairstyles and their corresponding prices
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# List of the number of each haircut sold last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate the average price of a haircut
total_price = sum(prices)  # Sum of all haircut prices
average_price = total_price / len(prices)  # Divide total by the number of hairstyles
print("Average Haircut Price:", average_price)

# Calculate new prices after applying a $5 discount to each haircut
new_prices = [price - 5 for price in prices]  # Create a new list with discounted prices
print("New Haircut Prices:", new_prices)

# Calculate the total revenue generated from all haircuts last week
total_revenue = sum(prices[i] * last_week[i] for i in range(len(hairstyles)))  # Multiply price and quantity for each haircut and sum
print("Total Revenue:", total_revenue)

# Calculate the average daily revenue from last week's sales
average_daily_revenue = total_revenue / 7  # Divide total revenue by 7 days
print("Average Daily Revenue:", average_daily_revenue)

# Find the hairstyles with prices under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]  # Create a list of hairstyles with prices below $30
print("Haircuts under $30:", cuts_under_30)
