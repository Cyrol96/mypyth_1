#1
topping = ["pepperoni", "pineaple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#2
prices = [2,6,1,3,2,7,2]

#3
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#4
num_pizzas = len(topping)
print(num_pizzas)

#5
print("we sell", num_two_dollar_slices, "dfferent kinds of pizza!")

#6
pizza_and_prices = [
    [prices[0], topping[0]],
    [prices[1], topping[1]],
    [prices[2], topping[2]],
    [prices[3], topping[3]],
    [prices[4], topping[4]],
    [prices[5], topping[5]],
    [prices[6], topping[6]],
]

#7
print(pizza_and_prices)

#8
pizza_and_prices.sort()
print(pizza_and_prices)

#9
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

#10 
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# 11
pizza_and_prices.pop()
print(pizza_and_prices)

#12
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# 13

three_cheapest = pizza_and_prices[:3]

# 14
print(three_cheapest)