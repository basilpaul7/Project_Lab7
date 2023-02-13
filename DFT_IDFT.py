#4A. DFT

import numpy as np
import matplotlib.pyplot as plt

N=4
D=np.empty((N,N),dtype=complex)
W=np.exp(-1j*2*np.pi/N) #Twiddle factor

for k in np.arange(N):
    for n in np.arange(N):
        D[k,n]=W**(k*n) #Twiddle factor matrix
np.round(D)

x=np.array([1,2,3,4]).T #Column vector
X=D @ x  #Matrix product

n=np.arange(0,N)
mag=np.zeros(N)
ph=np.zeros(N)

for k in np.arange(N):
    mag[k]=np.absolute(X[k])
    ph[k]=np.angle(X[k])

print("x(n)=",x)
print("X(k)=",np.round(X))

plt.title("Magnitude Spectrum") 
plt.xlabel("k")
plt.ylabel("|X(k)|")  
plt.stem(n,mag)
plt.show()

plt.title("Phase Spectrum") 
plt.xlabel("k")
plt.ylabel("<X(k)")    
plt.stem(n,ph)
plt.show()



#4B. IDFT

import numpy as np

N=4
D=np.empty((N,N),dtype=complex)
W=np.exp(1j*2*np.pi/N) #Twiddle factor

for k in np.arange(N):
   for n in np.arange(N):
       D[k,n]=W**(k*n) #Twiddle factor matrix
np.round(D)

X=np.array([10,-2+2j,-2,-2-2j]).T #Column vector
x=(1/N)* (D @ X)  #matrix product divided by N

print("X(k)=",X)
print("x(n)=",np.round(x))
