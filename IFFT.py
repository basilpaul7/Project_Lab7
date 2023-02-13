import numpy as np

def IFFT(X): 
    N = len(X)
    if N==1:
        return X
    else:
        x_even = IFFT(X[::2])
        x_odd = IFFT(X[1::2])
        factor = np.exp(2j*np.pi*np.arange(N)/N)

    x= np.concatenate(\
      [x_even+factor[:int (N/2)]*x_odd, x_even+factor[int (N/2):]*x_odd])
    return x

X=np.array([8, 0, 0, 0, 0, 0, 0, 0])
N=len(X)
x=np.round((1/N)*(IFFT(X)))
print ("X(k)=",X)
print("x[n] by IFFT=",x)
