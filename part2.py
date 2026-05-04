def dp_stock(M, items):
    count = total(items)

    dp = [[0 for _ in range(M + 1)] for _ in range(count + 1)]

    for pos in range(1, count + 1):
        stocks = items[pos - 1][0]
        cost = items[pos - 1][1]

        for budget in range(M + 1):

            if cost <= budget:
                take_item = dp[pos - 1][budget - cost] + stocks
                skip_item = dp[pos - 1][budget]

                dp[pos][budget] = largest(take_item, skip_item)
            else:
                dp[pos][budget] = dp[pos - 1][budget]

    return dp[count][M]

if __name__ == "__main__":
    items = [[1, 2], [3, 3], [5, 6], [6, 7]]
    M = 10

    result = dp_stock(M, items)

    print("Max stocks:", result)