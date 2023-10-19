fname = input("Enter file name: ")
#if no file name is given then it defaults to qwe.txt
if len(fname) < 1:
    fname = "qwe.txt"
fh = open(fname)
count = 0
# for loop to find the file starts with "from"
# if k doesn't start with "from "
for k in fh :    
    if not k.startswith("From "): continue
    else :
       count += 1
       f=k.split()
       print(f[1])
print("There were", count, "lines in the file with From as the first word")
