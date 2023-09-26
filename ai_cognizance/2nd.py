import numpy as np
# single dimensional array
a = np.array([1,2,3,4,5,6])
print(a,'\n')

# multi dimensional array
b = np.array([[1,2,3],[123,456,789]])
print(b,'\n')

# array of specified range
c = np.arange(36)
print(c,'\n')

# changing array dimesions
d = c.reshape(3,12)
print(d,'\n')

# inverse of multidimentional sq matix
e = np.random.rand(25)
e = e.reshape(5,5)
e_inv = np.linalg.inv(e)
print(e,'\n')
print(e_inv,"\n")

# extracting specific rows 
print(d[2, : ],"\n") # extracted last row
print(d[1,3],"\n") # extracted 2nd row and 3rd element


# Specify the file path
file_path = "ai_cognizance/data.txt"
# Use numpy.loadtxt() to read data from the file and create a NumPy ndarray
data_array = np.loadtxt(file_path)
print(data_array)
