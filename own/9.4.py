fname = input("Enter file name: ")
#if no file name is given then it defaults to qwe.txt
if len(fname) < 1:
    fname = "qwe.txt"
fh = open(fname)
c = list()
# for loop to find the file starts with "from"
# if k doesn't start with "from "
for k in fh :    
    if not k.startswith("From "): continue
    else :
       f=k.split()
       c.append(f[1])

a=dict()
count = 0
for words in c :
   q = words.split()
   count += 1
   for c in q :
    if c not in a:
      a[c] = 1  
    else :
      a[c] = a[c] + 1

bigcount = None
bigword = None
for word,count in a.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word    

print (bigword,bigcount)
