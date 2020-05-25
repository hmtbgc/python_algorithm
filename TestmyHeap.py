from myHeap import myHeap
import random
random.seed(10)

A = [2, 5, 3, 6, 8]
h = myHeap(A)
h.make_heap()
print(h)
# print(h.heapsort(ascend=False))
# print(h.heapsort(ascend=True))
print(A)

# B = [random.random() for i in range(20)]
# # print(B)
# hh = myHeap(B)
# hh.make_heap()
# print(hh.heapsort(ascend=True))

# print(h.pop_first())
# print(h)
# print(h.pop_first())
# print(h)
# print(h.pop_first())
# print(h)
# print(h.pop_first())
# print(h)
# print(h.pop_first())
# print(h)
# print(h.pop_first())
# print(h)

h.insert(7)
print(h)
print(h.pop_first())
print(h.pop_first())
print(h.pop_first())
print(h.pop_first())
print(h.pop_first())
print(h.pop_first())
print(h.pop_first())





 
