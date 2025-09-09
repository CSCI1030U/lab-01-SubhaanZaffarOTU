def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  
# We have to multiply these two numeric values in order to find the total cost before tax (subtotal_cost).
    subtotal_cost = cost_per_item * quantity
# Now we have to calculate how much tax the subtotal has, and we do this by multiplying the value by 13% (0.13).
    tax = subtotal_cost * 0.13
# Now we calculate the total cost after the tax is added, so we just add the two values of tax and subtotal cost.
    total_cost = subtotal_cost + tax

    # YOUR CODE FOR PART 2 GOES HERE
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')


    # THIS IS THE CODE FOR PART 3
    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth {} dollars.'.format(investment))
    # expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.

if __name__ == "__main__":
    main()
