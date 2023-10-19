n = 6000
lst = set()
for a in range(2,n+1,1):
    c = 0
    for b in range (2,n+1,1):
        if a%b == 0 :
            c += 1
       
    if c > 1 :
        None
    else:
        lst.add(a)
        
for all in lst :
    print(all,end = " ")