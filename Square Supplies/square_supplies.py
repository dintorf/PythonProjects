import math

def answer(n):
    # your code here
    num_pads = 0
    wallet = n
    while wallet:
        wallet -= int(math.sqrt(wallet))**2
        num_pads += 1

    return num_pads
