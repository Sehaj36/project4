# function cheack all the stocks to check for the best combinations
from itertools import combinations

def exhaustive_stock(M, items):
    # max stock
    best_stocks = 0   
    #best indices
    best_subsets = []

    length = len(items)
# goes throught all the subset sizes
    for r in range(length + 1):
# all pairs of size r
        for subset in combinations(range(length), r):
            total_cost = 0
            total_stocks = 0
#add total cost of the stock 
            for index in subset:
                total_stocks += items[index][0]
                total_cost += items[index][1]
#checks if its within budget

            if total_cost <= M and total_stocks > best_stocks:
                best_stocks = total_stocks
                best_subsets = subset

    return best_stocks, best_subsets

if __name__ == "__main__":
    items = [[1,2],[3,3],[5,6],[6,7]]
    M = 10

    result = exhaustive_stock(M, items)

    print("Max stocks:", result[0])
    print("Selected indices:", result[1])