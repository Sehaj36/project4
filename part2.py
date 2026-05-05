# function figures out the most stocks you can with out going over your budget
def dp_stocks(M, items):
    count = len(items)
# made a 2d table the rows will show items and the columns will show the budget
     dp = [[0 for _ in range(M + 1)] for _ in range(count + 1)]

    for pos in range(1, count + 1):
        stocks = items[pos - 1][0]
        cost = items[pos - 1][1]
# loops from each possible budget
        for budget in range(M + 1):
# check if the item will fit in the budget
              if cost <= budget:
                take_item = dp[pos - 1][budget - cost] + stocks
                skip_item = dp[pos - 1][budget]

                dp[pos][budget] = max(take_item, skip_item)
            else:
# if its over budget it will skip it
                dp[pos][budget] = dp[pos - 1][budget]

    return dp[count][M]


if __name__ == "__main__":
    # Sample input
    items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    M = 10

    result = dp_stocks(M, items)

    print("Max stocks:", result)