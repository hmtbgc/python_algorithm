from myhashtable import myhashtable

h = myhashtable()
h.add("mike", 1)
h.add("john", 2)
h.add("tom", 3)
print(h.search("mike"))
print(h.search("yeh"))
h.print_whole_hashtable()
h.clear()
for i in range(100):
    h.add(f"mike{i}", i)
print(h.search("mike45"))
h.print_whole_hashtable()
print(h.table_size())
print(h.num_size())

