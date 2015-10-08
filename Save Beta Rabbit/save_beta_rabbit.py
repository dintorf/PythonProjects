from functools import wraps

def answer(food, grid):
    # your code here
    @memoization
    def remainder(total, x, y):
        total -= grid[x][y]

        if x < 0 or y < 0 or total < 0:
            return food + 1
        elif x == y == 0:
            return total
        else:
            return min(remainder(total, x-1, y), remainder(total, x, y-1))

    left_overs = remainder(food, len(grid)-1, len(grid)-1)
    print left_overs
    return left_overs if left_overs <= food else -1

def memoization(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        try:
            result = cache[args]
        except KeyError:
            result = cache[args] = func(*args)
        return result
    return wrap
