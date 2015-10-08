def answer(words):
    # your code here
    g = graph(words)
    s = start(g)

    l = []
    v = []

    def next(n):
        if n not in v:
            v.append(n)

            if n in g:
                for e in g[n]:
                    next(e)

            l.append(n)

    for n in s:
        next(n)

    return "".join(l[::-1])

def graph(w):
    g = {}

    nrows = len(w)

    for r in range(nrows-1):
        e = find(w[r], w[r+1])

        if e is not None:
            n, d = e

            if n in g:
                g[n].append(d)
            else:
                g[n] = [d]

    return g

def find(x, y):
    size = min(len(x), len(y))

    for z in range(size):
        if x[z] != y[z]:
            return x[z], y[z]

def start(g):
    edges = set()

    for es in g.values():
        for e in es:
            edges.add(e)

    s = set()

    for n in g:
        if n not in edges:
            s.add(n)

    return s
