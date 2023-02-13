#2A. Energy of Signal
import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(1,4,4)
e=np.dot(x,x)

print("x(n)=",x)
print("Energy of x(n)=",e)



#2B.Linear Convolution

import numpy as np
import matplotlib.pyplot as plt

def conv(x,h):

    M= len(x)
    N = len(h)
    z=np.abs(N-M)
    K= max(N,M)
    YL=N+M-1
    y=np.zeros(YL)
    
    if M>N:
      h= np.append(h,np.zeros(z))   
    elif M<N:
      x = np.append(x,np.zeros(z))
        
    for i in range(YL):
      if i<M:
        for j in range(i+1):
              y[i]+=x[j]*h[i-j]
      elif i>=M:
        for j in range(K-1,i-K,-1):
              y[i]+=x[j]*h[i-j]
        
    return y[:YL]
   
x=np.random.randint(1,4,5)
h=np.random.randint(1,4,3)
y=conv(x,h)

nx=np.arange(0,len(x))
nh=np.arange(0,len(h))
ny=np.arange(0,len(y))

print("x(n)=",x)
print("h(n)=",h)
print("x(n)*h(n)=",y)
      
plt.xlabel("n")
plt.ylabel("x(n)")    
plt.stem(nx,x)
plt.show()

plt.xlabel("n")
plt.ylabel("h(n)")    
plt.stem(nh,h)
plt.show()

plt.xlabel("n")
plt.ylabel("x(n)*h(n)")    
plt.stem(ny,y)
plt.show()



#2C.Linear Correlation

import numpy as np
import matplotlib.pyplot as plt

def corr(x,h):

    M= len(x)
    N = len(h)
    z=np.abs(N-M)
    K= max(N,M)
    YL=N+M-1
    y=np.zeros(YL)

    h= h[::-1]

    if M>N:
      h= np.append(h,np.zeros(z))   
    elif M<N:
      x = np.append(x,np.zeros(z))
        
    for i in range(YL):
      if i<M:
        for j in range(i+1):
              y[i]+=x[j]*h[i-j]
      elif i>=M:
        for j in range(K-1,i-K,-1):
              y[i]+=x[j]*h[i-j]

    if len(h)>N or len(x)>M:
      return y[z::]
    else:
      return y   

x=np.random.randint(1,4,5)
h=np.random.randint(1,4,3)
y=corr(x,h)   

ny=np.arange(0,len(y))
nx=np.arange(0,len(x))
ny=np.arange(0,len(w))

print("x(n)=",x)
print("h(n)=",h)
print("Output=",y)
      
plt.xlabel("n")
plt.ylabel("y(n)")    
plt.stem(ny,y)
plt.show()

plt.xlabel("n")
plt.ylabel("x(n)")    
plt.stem(nx,x)
plt.show()

plt.xlabel("n")
plt.ylabel("y(n)")    
plt.stem(ny,y)
plt.show()

