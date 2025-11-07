from collections import Counter, ChainMap, deque, defaultdict, namedtuple, OrderedDict, UserDict, UserList, UserString

# Counter
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
c = Counter(words)
print(c.most_common(2)) # [("apple", 3), ("banana", 2)]
for w in c.elements(): # yields elements repeated
    print(w)

# Counter arithmetic
a = Counter(a=3, b=1)
b = Counter(a=1, b=2)
print(a + b)   # Counter({'a':4,'b':3})
print(a - b)   # Counter({'a':2})   # removes zero/neg counts


# ChainMap
# useful for layered configs, scopes

defaults = {'color':'red', 'user':'guest'}
env = {'user':'alice'}
cfg = ChainMap(env, defaults)
print("chainmap")
print(cfg)
cfg['user'] ='bob'
print(cfg)

# Caveat: writes go to the first mapping only.


# Defaultdict
d = defaultdict(int)
for x in range(5):
    d[x] += 1


# Deque

dq = deque([], 10) # max length set to 10
dq.append(1)
dq.appendleft(0)
print("Deque", dq)
dq.extend([2, 3, 4, 5, 6, 7, 8, 9, 10]) # drop zero as max length is 10 
print("Deque", dq)

print("rotating deque")
dq.rotate(1)
print(dq)
dq.rotate(-1)
print(dq)

# Best practices:
# Use deque for FIFO/LIFO instead of list when pops from left are needed.
# Avoid indexing in performance-critical loops.



# namedtuple
# lightweight immutable tuples with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(1, 2)
print(p)
p2 = p._replace(x=3) 
print(p2)
d = p._asdict()  # ordered dict of fields
print(d)

# Best practices
# Prefer dataclass (with frozen=True if immutability desired) for clarity, methods, defaults, and type checking.



# OrderedDict
# preserves insertion order for dict.

# LRU example
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, k):
        try:
            v = self.cache.pop(k)
            self.cache[k] = v  # reinsert as most-recent
            return v
        except KeyError:
            return -1
    
    def put(self, k, v):
        if k in self.cache:
            self.cache.pop(k)
        elif len(self.cache)>=self.capacity:
            self.cache.popitem(last=False)
        self.cache[k] = v


class CaseInsensitiveDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

