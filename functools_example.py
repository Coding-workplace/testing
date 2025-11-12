from functools import cached_property, partial, partialmethod, singledispatchmethod, cache, cmp_to_key, lru_cache, reduce, singledispatch, total_ordering, update_wrapper, wraps


@cache
def heavy(x):
    # deterministic expensive computation
    pass

@lru_cache
def heavy1():
    pass

@lru_cache(None) # same as @cache
def heavy2():
    pass

def expensive_fetch(id):
    pass

class DBRecord:
    @cached_property
    def computed(self):
        # expensive I/O/compute — runs once per instance
        return expensive_fetch(self.id)


def power(base, exp):
    return base ** exp

pow2 = partial(power, exp=2)
pow5 = partial(power, 5)         # base fixed to 5

print(pow2(3))  # 9
print(pow5(3))  # 125  -> calls power(5, 3)


class Painter:
    def paint(self, color, *, opacity=1.0):
        return f"paint {color} @ {opacity}"

set_red = partialmethod(Painter.paint, "red")

class P(Painter):
    red = set_red

print(P().red())  # "paint red @ 1.0"


# partial objects expose .func, .args, .keywords — useful for introspection.
# partial does not by default copy name/doc; use wraps/update_wrapper to transfer metadata.

# When to prefer over lambda: partial is clearer, faster, and exposes metadata.


def compare_by_last_char(a, b):
    return (a[-1] > b[-1]) - (a[-1] < b[-1])

items = ["apple", "banana", "cherry"]
sorted_items = sorted(items, key=cmp_to_key(compare_by_last_char))
print(sorted_items)


print(reduce(lambda x,y:x+y, [1, 2, 3, 4, 5]))


@singledispatch
def process(obj):
    return f"default {obj!r}"

@process.register(int)
def _(n: int):
    return f"int {n}"

@process.register(list)
def _(lst: list):
    return f"list len={len(lst)}"

print(process(1))       # uses int
print(process([1,2]))   # uses list
print(process("s"))     # default


@total_ordering
class Ver:
    def __init__(self, v): self.v = v
    def __eq___(self, other): return self.v == other.v
    def __lt__(self, other): return self.v<other.v

# Caveat: generated methods use the provided ones; implement them correctly and efficiently.


def power(a, b):
    '''a to the power b'''
    return a ** b

pow2 = partial(power, b=2)
pow2.__doc__ = 'a to the power 2'
pow2.__name__ = 'pow2'

print('Before update:')
print('Doc:', pow2.__doc__)
print('Name:', pow2.__name__)

update_wrapper(pow2, power)

print('After update:')
print('Doc:', pow2.__doc__)
print('Name:', pow2.__name__)



def decorator(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        """Decorator's docstring"""
        return f(*args, **kwargs)
    print('Docstring:', decorated.__doc__)
    return decorated

@decorator
def f(x):
    """f's Docstring"""
    return x
print('Function name:', f.__name__)
print('Docstring:', f.__doc__)

# Tip: include qualname in assignment to make stack traces/readable reprs consistent.


