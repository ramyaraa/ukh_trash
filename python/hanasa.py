foods = []
prices = []
amounts = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    
    if food.lower() == "q":
        break
    
        
        
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        amount = int(input("how many do you need? "))
        foods.append(food)
        prices.append(price)
        amounts.append(amount)

print("----- YOUR CART -----")

for food in foods:
    print(food )
for price in prices:
    print(price)
for amount in amounts:
    print(amount)

for price in prices:
    total += price * amount

print()
print(f"Your total is: ${total}")
