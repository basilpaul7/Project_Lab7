#trapezoid
import numpy as np
import matplotlib.pyplot as plt

def trapezoid(a, b, c): 
    n=np.arange(a,b)
    x=np.zeros_like(n)
    x[(n>=-c)&(n<=c)]=2
    x[(n>=a)&(n<-c)]=(-a+n[(n>=a)&(n<-c)])
    x[(n>c)&(n<-a)]=(-a+n[(n>c)&(n<-a)])
    plt.plot(n, x)
    plt.show() 
trapezoid(-3,4,2)



#inverse trapezoid
import numpy as np
import matplotlib.pyplot as plt

def trapezoid(a, b, c): 
    n=np.arange(a,b)
    x=np.zeros_like(n)
    x[(n>=-c)&(n<=c)]=-2
    x[(n>=a)&(n<-c)]=-(-a+n[(n>=a)&(n<-c)])
    x[(n>c)&(n<-a)]=-(-a+n[(n>c)&(n<-a)])
    plt.plot(n, x)
    plt.show() 
trapezoid(-3,4,2)
