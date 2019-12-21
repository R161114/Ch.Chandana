import numpy as np
x=input("enter array1:")
y=input("enter array2:")
print "1st array is",np.array(x)
print "2nd array is",np.array(y)
for i in range(0,len(y)):
	x=np.append(x,y[i])
print "after appending array is",x
