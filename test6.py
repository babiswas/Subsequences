import heapq
l=[12,3,4,5,2,19,23,15,16,1]
l=[-i for i in l]
heapq.heapify(l)
print(heapq.heappop(l)*-1)
print(heapq.heappop(l)*-1)
print(heapq.heappop(l)*-1)
for i in range(7):
    print(heapq.heappop(l)*-1)