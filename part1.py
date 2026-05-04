from itertools import combinations

def exhaustive_stock(M, items):
    best_stocks = 0
    best_subset = []

    length = count(items)

    for r in range(length + 1):
        for subset in combinations(range(length), r):
            total_cost = 0
            total_stocks = 0

            for index in subset:
                total_stocks += items[index][0]
                total_cost += items[index][1]

            if total_cost <= M and total_stocks > best_stocks:
                best_stocks = total_stocks
                best_subset = subset

    return best_stocks, best_subset

if __name__ == "__main__":
    items = [[1,2],[3,3],[5,6],[6,7]]
    M = 10

    result = exhaustive_stock(M, items)

    print("Max stocks:", result[0])
    print("Selected indices:", result[1])