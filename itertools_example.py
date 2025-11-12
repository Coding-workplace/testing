import itertools

# count + islice to get first 10 even numbers starting at 0
evens = itertools.islice(itertools.count(0, 2), 10)
print(list(evens)) # [0, 2, 4, ... , 18]

print(list(itertools.repeat('A', 3)))        # ['A','A','A']
print(list(itertools.islice(itertools.cycle('AB'), 6)))  # ['A','B','A','B','A','B']
print(list(itertools.chain('ABC', 'DE')))    # ['A','B','C','D','E']

print(list(itertools.accumulate([1, 2, 3, 4, 5, 6]))) # [1, 3, 6, 10, 15, 21]
print(list(itertools.accumulate([1, 2, 3, 4, 5, 6], lambda x, y: x*y)))  # [1, 2, 6, 24, 120, 720]

print(list(itertools.batched("ABCDEFG", 3))) # [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]



li1 = [1, 4, 5, 7]   
li2 = [1, 6, 5, 9]   
li3 = [8, 10, 5, 4] 
  
# initializing list of list 
li4 = [li1, li2, li3] 

# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain.from_iterable(li4)))


# Filtering
data = [1,4,6,3,8]
print(list(itertools.filterfalse(lambda x: x<5, data)))  # [6,8]
print(list(itertools.compress(['a','b','c'], [1,0,1])))  # ['a','c']
print(list(itertools.takewhile(lambda x: x<5, [1,2,3,6,1])))  # [1,2,3]
print(list(itertools.dropwhile(lambda x: x<5, [1,2,3,6,1])))  # [6, 1]


# pairwise

numbers = [1, 2, 3, 4, 5]
print(list(itertools.pairwise(numbers))) # [(1, 2), (2, 3), (3, 4), (4, 5)]


# starmap
pairs = [(2,5), (3,2), (10,3)]
print(list(itertools.starmap(pow, pairs)))  # [32, 9, 1000]

it = iter([1,2,3])
a,b = itertools.tee(it, 2)
print(list(a), list(b))  # both [1,2,3]
# Note: tee buffers data; if one branch advances far ahead, memory grows.

items = [1,1,2,2,1,1]
for key, group in itertools.groupby(items):
    print(key, list(group))
# 1 [1,1]
# 2 [2,2]
# 1 [1,1]
# Important: input must be sorted by key to group logical groups.

print(list(itertools.product('AB', repeat=2)))          # [('A','A'),('A','B'),...]
print(list(itertools.permutations('ABC', 2)))           # ordered arrangements
print(list(itertools.combinations('ABC', 2)))           # unordered pairs, no repeats
print(list(itertools.combinations_with_replacement('AB', 2)))  # allow repeats


# zip_longest - parallel iteration with fill
print(list(itertools.zip_longest([1,2,3], ['a','b'], fillvalue='-')))  # [(1,'a'),(2,'b'),(3,'-')]

# Grouper (fixed-size chunks, fillvalue optional):
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)
# Example: list(grouper('ABCDEFG', 3, 'x')) -> [('A','B','C'),('D','E','F'),('G','x','x')]


