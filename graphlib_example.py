from graphlib import TopologicalSorter
from concurrent.futures import ThreadPoolExecutor

graph = {
    "build": {"compile", "generate"},
    "compile": {"parse"},
    "generate": {"parse"},
    "parse": set()
}

ts = TopologicalSorter(graph)
order = list(ts.static_order())
print(order)  # e.g. ['parse', 'compile', 'generate', 'build']



graph = {
    "A": {"B", "C"},
    "B": {"D"},
    "C": {"D"},
    "D": set()
}

ts = TopologicalSorter(graph)
ts.prepare()
results = {}

with ThreadPoolExecutor(max_workers=4) as ex:
    while ts.is_active():
        ready = ts.get_ready()            # nodes ready to run in parallel
        futures = {ex.submit(lambda n: n+"-done", n): n for n in ready}
        for fut in futures:
            results[futures[fut]] = fut.result()
        ts.done(*ready)
print(results)  # processed results for all nodes


# Building incrementally
ts = TopologicalSorter()
ts.add("pkgA", "pkgB", "pkgC")
ts.add("pkgB", "pkgC")
ts.add("pkgC")   # no predecessors
print(list(ts.static_order()))  # e.g. ['pkgC', 'pkgB', 'pkgA']

# Cycle detection

from graphlib import TopologicalSorter, CycleError
g = {"x": {"y"}, "y": {"x"}}
try:
    TopologicalSorter(g).prepare()
except CycleError as e:
    print("Cycle detected:", e.args[1])  # cycle nodes list
