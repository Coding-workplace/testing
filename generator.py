def accumulator():
    total = 0
    while True:
        add = yield total
        if add is None:
            break
        total += add

from inspect import getgeneratorstate as ggs
g = accumulator()
next(g)      # primes, returns 0
print(help(g.send))
print(help(g.throw))
print(help(g.close))
print(g.close())
