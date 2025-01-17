import numpy as np
from ElibV3 import E2d
#positions
n = 4000
k=6
t= np.linspace(0,2*np.pi,n)
r = np.cos(k*t)
xpos = r*np.cos(t)
ypos = r*np.sin(t)
#charge
qs = np.arange(0,n*np.pi,np.pi)
q = np.cos(qs)
#make grid
u = np.arange(-2,2,0.01)
x,y = np.meshgrid(u,u)
#E field
Ex,Ey = E2d(x,y,q,xpos,ypos)[:2]
#reshape E field for matplotlib 
Ex,Ey = Ex.reshape(x.shape),Ey.reshape(y.shape)
#plot 2d vector field
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
colors = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(x, y, Ex,Ey,density=2.5,color=colors,cmap=plt.cm.plasma)
for i in range(len(xpos)):
        if q[i] > 0: 
            ax.plot(xpos[i],ypos[i],marker='o',c="#4CC9F0")
        else:
            ax.plot(xpos[i],ypos[i],marker='o',c="#F72585")
plt.show()