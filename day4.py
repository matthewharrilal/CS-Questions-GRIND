# def get_max_profit(stock_prices):
#     max_profit = stock_prices[1] - stock_prices[0] # Calculate the first difference in profit
#     current_min = stock_prices[0]

#     for index in range(0, len(stock_prices)):
#         current_price = stock_prices[index]
#         potential_profit = current_price - current_min # Calculate the profit at any given step
#         current_min = min(current_price, current_min) # Update the minimum price between our given min and current price
#         max_profit = max(max_profit, potential_profit) # Same logic for the profit

#     return max_profit


def get_max_profit(stock_prices_yesterday):

    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # min_price = stock_prices_yesterday[0]
    # max_profit = 0

    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    print("")
    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        print("   cur_price %s min_price %s pot_profit %s max_profit %s" %
              (current_price, min_price, potential_profit, max_profit))

    return max_profit

print(get_max_profit([9, 7, 4, 1]))