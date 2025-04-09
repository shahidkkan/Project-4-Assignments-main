def pop_up_shop():
    fruits = {
    "Apple":100,
    "Banana":200,
    "Orange":100,
    "Mango":150,
    } 
    total_cost = 0
    for fruits_name in fruits:
      price = fruits[fruits_name]
      amount = int(input(f"How Many ({fruits_name}) do you want to buy?: "))
      total_cost += (price * amount)
    print(f"Your Total is ${total_cost}")

pop_up_shop()
