#7. Linear Convolution by Overlap Save Method

import numpy as np
from scipy.fft import fft, ifft

x=[3,-1,0,1,3,2,0,1,2,1]
TL=len(x)
h=[1,1,1]
M=len(h)      
y=[]
N=2*M-1 

#h=np.append(h,np.zeros(M-1))
#x=np.append(x,np.zeros(M-TL%M))

b=int(np.ceil(TL/M)) #Total No of blocks

for i in np.arange(b):
  if i==0:
    xi=np.append(np.zeros(M-1),x[0:M])

  else:
    xi=x[i*M-(M-1):(i+1)*M]
  
  #Discarding first M-1 terms
  yn=ifft(fft(xi,N)*fft(h,N))
  yi=yn[M-1:2*M-1]
  y=np.append(y,yi)

print("x(n):",x)
print("h(n):",h)
print("By overlap save, x(n)*h(n)=",np.real(y))
