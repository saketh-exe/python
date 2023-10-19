trg = 15
trglis = list()
lis1  = lis2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for a in lis1:
    for b in lis2:
        if a+b == trg :
            c = (a,b)
            trglis.append(c)
            

print(trglis)

