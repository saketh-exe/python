import statistics as s
import sys as r
x = 1
lst = list()
while x != 5:
    c = r.argv[0:]
    x += 1
    if c not in lst:
        lst.append(c)



print(s.mean(lst))