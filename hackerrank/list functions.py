n = int(input())
l = list()
for i in range (n):
    a = input()
    b=a.split()
    if b[0] == "insert" :
        q = int(b[1])
        l.insert(q,int(b[2]))
    elif b[0] == "remove" :
        l.remove(int(b[1]))
    elif b[0] == "append" :
        l.append(int(b[1]))
    elif b[0] == "sort" : l.sort()
    elif b[0] == "reverse" : l.reverse()
    elif b[0] == "pop" : l.pop()
    elif b[0] == "print" : print(l)