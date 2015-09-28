def answer(x):
    # your code here
    distinct_codes = []
    for code in x:
        if code not in distinct_codes and code[::-1] not in distinct_codes:
            distinct_codes.append(code)

    return len(distinct_codes)
