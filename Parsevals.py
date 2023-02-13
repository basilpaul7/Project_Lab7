#parsevals theorem
import numpy as np
import matplotlib.pyplot as plt

def dft_mtx(N):
    D=np.empty((N,N), dtype=np.cdouble)
    W=np.exp(-1j*2*np.pi/N) 
    k=np.arange(N)
    for n in np.arange(N):
        D[:,n]=W**(n*k)
    return (np.round(D))

x=np.array([1,1+1j,-1,1-1j])
N=len(x)
D=dft_mtx(N)
X=D@x
X=np.round(X)

mag_x=np.abs(x)
square_x=np.dot(mag_x, mag_x) 
print("square x" ,square_x)

mag_X=np.abs(X)
square_X=np.dot(mag_X, mag_X) 
print("square X", square_X)

if (square_x==square_X): 
    print("theorem verified")
else:
    print("not verified")
