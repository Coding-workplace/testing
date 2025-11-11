import ctypes
import weakref
import gc

# list object which is referenced by
# my_list
my_list = [1, 2, 3]

# finding the id of list object
my_list_address = id(my_list)

# finds reference count of my_list
ref_count = ctypes.c_long.from_address(my_list_address).value

print(f"Reference count for my_list is: {ref_count}")


class Obj:
    def __init__(self, name):
        self.name = name    
    def __repr__(self):
        return f"obj({self.name})"
    
o = Obj("A")

def on_dead(wr):
    print("finalizer callback: referent gone:", wr)

wr = weakref.ref(o, on_dead)
print("alive:", wr())
del o
gc.collect()
print("after GC:", wr())




class Data:
    def __init__(self, v): self.v = v
    def __repr__(self): return f"Data({self.v})"

cache = weakref.WeakValueDictionary()
d = Data(10)
cache['x'] = d
print(cache.get('x'))
del d
gc.collect()
print(cache.get('x'))


class Node: pass
meta = weakref.WeakKeyDictionary()
n = Node()
meta[n] = {"created": "now"}
print(list(meta.items()))
del n
gc.collect()
print(list(meta.items()))


class X:
    def greet(self): return "hello"
x = X()
p = weakref.proxy(x)
print(p.greet())   # "hello"
del x
gc.collect()
try:
    p.greet()
except ReferenceError:
    print("referent gone -> ReferenceError")


class Resource: pass

r = Resource()
f = weakref.finalize(r, print, "cleaning up resource")
print(f.alive)   # True
del r
gc.collect()
print(f.alive)   # False, callback ran
