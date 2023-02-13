#linearconvolution2
import numpy as np
import matplotlib.pyplot as plt

k=int(input("Enter k :" )) 
x=np.random.randint (1, 10, k)
m=int (input("Enter m :"))
h=np.random.randint (1, 10, m)

N=k+m-1 
y=np.zeros(N)
print (h)
print (x)

if (k>=m):
    for i in np.arange(N): 
        if (i<m):
            y[i]=np.dot(x[0:i+1], h[i::-1])
        elif (i<k):
            y[i]=np.dot(x[i-m+1:i+1], h[::-1])
        else:
            y[i]=np.dot(x[i-m+1:], h[m:i-k:-1])

if (k<m):
    for ii in np.arange(N) :
        if (i<k):
            y[i]=np.dot(h[0:i+1],x[i::-1])
        elif (ii<m):
            y[i]=np.dot(h[i-k+1:i+1], x[::-1])
        else:
            y[i]=np.dot(h[i-k+1:], x[k:i-m:-1])

print (y)
