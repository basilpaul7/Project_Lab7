#Linear using circular
import numpy as np
import matplotlib.pyplot as plt
def circconvolve(x,y,N):
    N=len(x)
    y_revr=y[::-1]
    X=np.empty((N,N))
    for k in np.arange(N): 
        X[N-1-k]=np.roll(x,k)
    z= X@y_revr
    return z
def lnr_using_circ(x,y): 
    N=len(x)+len(y)-1 
    x=np.pad(x,[0,N-len(x)]) 
    y=np.pad (y,[0,N-len(y)]) 
    z= circconvolve(x,y,N)
    return z

x=np.array([1,2,3])
y=np.array([1,1,-1])
z=lnr_using_circ(x,y)
print(z)
