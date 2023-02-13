#5A. FFT & IFFT

import numpy as np
import matplotlib.pyplot as plt

def FFT(x):
    N = len(x)
    if N == 1:
        return x
    else:
      X_even = FFT(x[::2])
      X_odd = FFT(x[1::2])
      factor = np.exp(-2j*np.pi*np.arange(N)/ N)
      X = np.concatenate([X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])

    return X

def IFFT(k):
  k=np.array(k,dtype=complex)
  kconj=np.conjugate(k)
  X=FFT(kconj)
  x=np.conjugate(X)
  x=x/k.shape[0]

  return np.round(x)

x=np.random.randint(0,10,32)
X=np.round(FFT(x)) 
print("x(n)=",x)
print("X(k)=",X) 
print("x(n) by IFFT=",IFFT(X))    

#Magnitude & Phase spectrum
N=len(x)
mag=np.zeros(N)
ph=np.zeros(N)
n=np.arange(N)
for k in np.arange(N):
    mag[k]=np.absolute(X[k])
    ph[k]=np.angle(X[k])

plt.title("Magnitude Spectrum") 
plt.xlabel("k")
plt.ylabel("|X(k)|")  
plt.stem(n,mag, markerfmt=" ", basefmt="-b")
plt.show()

plt.title("Phase Spectrum") 
plt.xlabel("k")
plt.ylabel("<X(k)")    
plt.stem(n,ph,markerfmt=" ", basefmt="-b")
plt.show()



#5B. FFT with sampling Rate. Plot amplitude spectrum for both 2-sided and 1-sided frequencies

import numpy as np
import matplotlib.pyplot as plt

def FFT(x):
    N = len(x)
    if N == 1:
        return x
    else:
      X_even = FFT(x[::2])
      X_odd = FFT(x[1::2])
      factor = np.exp(-2j*np.pi*np.arange(N)/ N)
      X = np.concatenate([X_even+factor[:int(N/2)]*X_odd, X_even+factor[int(N/2):]*X_odd])

    return X    

#With sampling
sr = 128  # sampling rate
ts = 1.0/sr #sampling interval
t = np.arange(0,1,ts)

freq = 1
x = 3*np.sin(2*np.pi*freq*t)

freq = 4
x += np.sin(2*np.pi*freq*t)

freq = 7   
x += 0.5*np.sin(2*np.pi*freq*t)

plt.plot(t,x)
plt.ylabel('Amplitude')
plt.show()

X=np.round(FFT(x))

#One-side and two-side frequency plots
#Calculate the frequency
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T 

plt.stem(freq, abs(X), markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.show()

# Get the one-sided specturm and frequency
n_oneside = N//2
f_oneside = freq[:n_oneside]

# normalize the amplitude
X_oneside =X[:n_oneside]/n_oneside

plt.stem(f_oneside, abs(X_oneside), markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('Normalized FFT Amplitude |X(freq)|')
plt.show()




