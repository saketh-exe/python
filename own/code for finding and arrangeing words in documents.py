fname = input("Enter file name: ")
# reads the file
fh = open(fname)
# creates an empty list 
lst = list()
# for loop for spliting and striping the words in the document and it comes out as a list 
for line in fh:
    words = line.rstrip().split()
 # again for loop for searching the element in he words and adding them to the empty list    
    for element in words :
        if element in lst : continue
        else: lst.append(element)
# sorts the list     
lst.sort()
print(lst)