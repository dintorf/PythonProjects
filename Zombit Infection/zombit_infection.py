def answer(population, x, y, strength):
    # your code here
    result = []
    for y in population:
        row = []
        for x in y:
            x <= strength and row.append(-1) or row.append(x)
        result.append(row)

    print result

answer([[1, 2, 3], [2, 3, 4], [3, 2, 1]],0,0,2)
