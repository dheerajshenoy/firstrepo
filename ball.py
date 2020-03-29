import matplotlib.pyplot as plt 
import numpy as np 



def func(t,count):
    
    E = 0.9
    g = 9.8
    y = -(E**count)*g*(t**2)/2
    return y 

t = np.linspace(0,20)
d = 0
for i in range(len(t)):
    y = func(t,2*i)
    if(y[i] < 1):
        d+=1    
    if(d == 20):
        print(i)
        break
    
    if(t[i] == 0):
        plt.plot(-0,10,'.b')
    
    elif(y[i] < 0):
        plt.plot(-t[i],-y[i],'.b')
    else:
        plt.plot(-t[i],y[i],'.b')
        
plt.show()
