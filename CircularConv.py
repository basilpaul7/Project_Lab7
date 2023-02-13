#3. CIRCULAR CONVOLUTION

import numpy as np

def circonv(x,h): 
  M= len(x)
  N = len(h)
  z=np.abs(N-M)
  
  if M>N:
    h= np.append(h,np.zeros(z))   
  elif M<N:
     x = np.append(x,np.zeros(z))

  y=[]
  u=[]

  a=np.array(x[0])
  b=np.array(x[:0:-1])
  p=np.insert(b,0,a)
  y.append(p)
  for i in range(len(x)-1):
    p = np.roll(p,1)
    y.append(p)
  
  for t in y:
    u.append(np.dot(t,h))
    
  return u

x=np.random.randint(1,4,5)
h=np.random.randint(1,4,3)
y=circonv(x,h)

print("x(n)=",x)
print("h(n)=",h)
print("x(n)*h(n)=",y)
