a=[1,2,3,4,56,-4,-5,-42]
x=[]
y=[]
for i in a:
    if i<0:
        y.append(i)
    else:
        x.append(i)


for i in x:
    print(i,end=" ")
for k in y:
    print(k,end=" ")    
