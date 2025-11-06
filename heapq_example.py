import heapq
data = [19, 9, 4, 10, 11, 8, 2]
heapq.heapify(data)   # transforms list into min-heap
# smallest at data[0]

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
smallest = heapq.heappop(heap)  # 1
print(smallest)


res = heapq.heappushpop(heap, 2)
print(res)
# If 2 <= heap[0] result is 2 (push then pop returns smaller of new and root),
# otherwise returns old smallest and leaves 2 on heap.


old = heapq.heapreplace(heap, 7)
# returns popped smallest, pushes 7; useful for fixed-size heaps
# replace directlly


top3 = heapq.nlargest(3, [3, 2, 3, 53, 2, 5, 3, 7, 8])   # returns list sorted descending
bottom3 = heapq.nsmallest(3, [1, 2, 4, 5, 0])  # sorted ascending
# Optional key= argument supported

print(top3, bottom3)