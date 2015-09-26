def answer(numbers):
    # your code here
    pirates = []

    visited = 0

    while True:

        if visited in pirates:
            return len(pirates) - pirates.index(visited)

        pirates.append(visited)

        visited = numbers[visited]
