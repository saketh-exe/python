fhand = input()
qwe= open(fhand)
a = dict()
count = 0
for words in qwe :
   q = words.split()
   count += 1
   for c in q :
    if c not in a:
      a[c] = 1  
    else :
      a[c] = a[c] + 1

print(a)
print(count)


for word in q:
  q[a] = q.get(a,0) + 1

print(q)    



