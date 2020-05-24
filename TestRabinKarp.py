from RabinKarp import RabinKarp

string = "abrbadrabrd"
pattern = "abr"
rabinkarp = RabinKarp()
m, n = len(pattern), len(string)
print(rabinkarp.single_string_search(string, pattern))
