import copy
from collections import namedtuple

# Shallow copy of a list
a = [[1,2], [3,4]]
b = copy.copy(a)
print(b is a)              # False (different outer list)
print(b[0] is a[0])        # True  (inner lists are the same)

# Deep copy of a list
c = copy.deepcopy(a)
print(c is a)              # False
print(c[0] is a[0])        # False (inner lists duplicated)


class Node:
    def __init__(self, val, child=None):
        self.val = val
        self.child = child

n1 = Node(1)
n2 = Node(2, child=n1)
n1.child = n2  # create recursive reference

s = [n1, n2]
sh = copy.copy(s)
sh[0].val = 99
print(s[0].val)  # 99 (shared inner objects)

a = []
a.append(a)
d = copy.deepcopy(a)   # succeeds thanks to memo dict
print(d is d[0])              # True (structure preserved, new objects)


Person = namedtuple('Person', ['name', 'age'])
person = Person(name='Alice', age=30)
print(person)
updated_person = copy.replace(person, age=31)
print(updated_person)