import numpy as np
import matplotlib.pyplot as plt 


for t in range(0,21):
    y = -10*np.sin(t)
    if(y<0):
        plt.plot(t,-y,'.b')
    else:
        plt.plot(t,y,'.b')
plt.show()
