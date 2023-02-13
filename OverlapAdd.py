#Linear Convolution by Overlap Add Method

import numpy as np
from scipy.fft import fft, ifft
x = np.array([1,2,-1,2,3,-2,-3,-1,1,1,2,-1])
h = np.array([1,2])

M = len(h) #lengh of h
XL = len(x) #length of input sequence
FL = M+XL-1 #required length of the final convoluted sequence

N = 2*M-1 #size of each block
B = int(np.ceil(XL/M)) #number of blocks

Yi = np.zeros(FL+M-1) #to store the final sequence

for i in np.arange(B):
  Xi = x[i*M : (i+1)*M] #extracting each group
  y = np.real(np.round(ifft(np.multiply(fft(h,N), fft(Xi,N))))) #output of each block
  Yi[i*M:i*M+N] += y  #adding and storing the required points

#if len(Yi)>FL:
  #Yi = Yi[:FL] #discarding extra points if any
print ('The output sequence is:',Yi)
